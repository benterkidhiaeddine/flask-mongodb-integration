from flask_restx import fields, Resource, Api
from .crud import get_books, insert_book

api: Api = Api()


# Define an API model for book data
book_model = api.model(
    "Book",
    {
        "name": fields.String(required=True, description="The name of the book"),
    },
)


@api.route("/books")
class Book(Resource):
    @api.marshal_with(book_model, as_list=True)  # Specify the response model
    def get(self):
        # Retrieve a list of books (you may need to implement this logic)
        books = get_books()
        return books

    @api.doc("create book")
    @api.marshal_with(book_model, code=201)
    @api.expect(book_model)
    def post(self):
        return insert_book(api.payload), 201
