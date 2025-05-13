import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from orders import list_orders, retrieve_order, add_order, delete_order
from metals import update_metal


class JSONServer(HandleRequests):
    def do_GET(self):
        try:
            print(f"Received GET request for: {self.path}")
            response_body = ""
            url = self.parse_url(self.path)
            print(f"Parsed URL result: {url}")
            print(f"Type of url: {type(url)}")
            print(
                f"Keys in url: {url.keys() if hasattr(url, 'keys') else 'Not a dict'}"
            )
            if url["requested_resource"] == "orders":
                if url["pk"] != 0:
                    response_body = retrieve_order(url["pk"])
                    return self.response(response_body, status.HTTP_200_SUCCESS.value)
                response_body = list_orders()
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            else:
                return self.response(
                    "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
                )
        except Exception as e:
            print(f"Error handling request: {e}")
            import traceback

            traceback.print_exc()

    def do_POST(self):
        """Handle POST requests from a client"""

        url = self.parse_url(self.path)
        print(f"Parsed URL result: {url}")
        print(f"Type of url: {type(url)}")
        print(f"Keys in url: {url.keys() if hasattr(url, 'keys') else 'Not a dict'}")
        content_len = int(self.headers.get("content-length", 0))
        new_order_data = self.rfile.read(content_len)
        new_order_data = json.loads(new_order_data)

        if url["requested_resource"] == "orders":
            successfully_posted = add_order(new_order_data)
            if successfully_posted:
                return self.response("posted!", status.HTTP_201_SUCCESS_CREATED.value)

            return self.response(
                "Requested resource not found",
                status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
            )
        else:
            return self.response(
                "Not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def do_DELETE(self):

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "orders":
            if pk != 0:
                successfully_deleted = delete_order(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        else:
            return self.response(
                "Not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def do_PUT(self):
        url = self.parse_url(self.path)
        pk = url["pk"]

        content_len = int(self.headers.get("content-length", 0))
        new_price = self.rfile.read(content_len)
        new_price = json.loads(new_price)

        if url["requested_resource"] == "metals":
            if pk != 0:
                successfully_updated = update_metal(pk, new_price)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )

        else:
            return self.response(
                "Not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )


if __name__ == "__main__":
    host = ""
    port = 8088
    print(f"Starting server on http://localhost:{port}")
    print("Server is running... Press Ctrl+C to stop")
    HTTPServer((host, port), JSONServer).serve_forever()
