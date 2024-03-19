from rest_framework import serializers
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64
from javoblar.topshiriq__3.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            # 'id',
            'title',
            'content',
            'price',
            'margin',
            'package_code',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Define your AES key and initialization vector (IV)
        key = get_random_bytes(16)
        iv = get_random_bytes(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        fields_to_encrypt = ['price', 'margin', 'package_code']

        for field_name in fields_to_encrypt:
            field_value = str(representation.get())

            padded_data = pad(field_value.encode(), AES.block_size)

            encrypted_data = cipher.encrypt(padded_data)

            encrypted_data_base64 = base64.b64encode(encrypted_data).decode()

            representation[field_name] = encrypted_data_base64

        # Include key and IV in the response for decryption on the client side
        representation['encryption_key'] = base64.b64encode(key).decode()
        representation['iv'] = base64.b64encode(iv).decode()

        return representation
