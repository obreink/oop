class User:
    def __init__(self,username,password):
        self.username =username
        self._password = password


    def validate_password(self,password):
        contains_digit =any(char.isDigit() for char in password)
        contains_upper =any(char.isUpper() for char in password)
        contains_lower = any(char.isLower() for char in password)

        if not contains_digit:

            return False

        if not contains_upper:
            return False

        if not



















if __name__== "__main__":
    user1= User()
    user1.password



