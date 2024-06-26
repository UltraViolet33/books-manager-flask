from .. import db



books_authors_table = db.Table("books_authors",
                               db.Column("book_id", db.Integer,
                                         db.ForeignKey("books.id")),
                               db.Column("author_id", db.Integer,
                                         db.ForeignKey("authors.id"))
                               )


books_categories_table = db.Table("books_categories",
                                  db.Column("category_id", db.Integer,
                                            db.ForeignKey("categories.id")),
                                  db.Column("book_id", db.Integer,
                                            db.ForeignKey("books.id"))
                                  )


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    image_link = db.Column(db.String(150), nullable=True)
    summary = db.Column(db.String(500), nullable=True)

    authors = db.relationship(
        "Author", secondary=books_authors_table, backref="books")

    categories = db.relationship(
        "Category", secondary=books_categories_table, backref="books")

    def __init__(self, title, image_link, summary=""):
        self.title = title
        self.image_link = image_link
        self.summary = summary


    def get_single_book(book_id, current_user):
        book =  Book.query.filter_by(id=book_id).first()
        print(book)
        book.is_in_reading_list = False
        book.is_in_read_list = False
        book.is_in_progress = False


        
        for user in book.users_reading_list:
            if user.id == current_user.id:
                book.is_in_reading_list = True
        
        for user in book.users_read_list:
            if user.id == current_user.id:
                book.is_in_read_list = True

        for user in book.users_reading_inprogress:
            if user.id == current_user.id:
                book.is_in_progress = True
        
        return book