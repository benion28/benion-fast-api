from flask import jsonify


class ApiResponse:

    @staticmethod
    def _format_response(
        success: bool,
        message=None,
        data=None,
        error=None,
        status_code=200,
        pagination=None
    ):
        response = {
            "success": success,
            "status_code": status_code
        }

        if message is not None:
            response["message"] = message

        if data is not None:
            response["data"] = data

        if pagination is not None:
            response["pagination"] = pagination

        if error is not None:
            response["error"] = error

        return response, status_code

    @classmethod
    def success(cls, data=None, message="Successful", status_code=200, pagination=None):
        response, code = cls._format_response(
            success=True,
            message=message,
            data=data,
            status_code=status_code,
            pagination=pagination
        )
        return jsonify(response), code

    @classmethod
    def error(cls, error="Bad Request", status_code=400, data=None):
        response, code = cls._format_response(
            success=False,
            error=error,
            data=data,
            status_code=status_code
        )
        return jsonify(response), code
