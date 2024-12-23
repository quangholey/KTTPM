from .extension import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'phone_numbers')


class CatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class ImgSchema(ma.Schema):
    class Meta:
        fields = ( 'book_id','image_data')

# class BorrowSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'book_id', 'student_id', 'borrow_date', 'return_date')


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'page_count', 'author_id', 'category_id')

# class ImageSchema(ma.Schema):
#     class Meta:
#         fields = ('id')

class CartSchema(ma.Schema):
    class Meta:
        fields = ('id', 'book_id','user_id','price', 'quantity')

class Hoa_DonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'book_id', 'quantity', 'price', 'information', 'address', 'phone_number', 'sum_price', 'tt_hoadon', 'date')

class AfterCartSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'book_id', 'quantity', 'price', 'information')