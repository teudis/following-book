from rest_framework import serializers

from bookcore.models import Book, Language, Category, Author

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class AuthorSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSeiralizer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Book
        fields = "__all__"