from nebpysdk.src.core.Transaction import Transaction
import base64


class transactiontest:

    def __init__(self):
        pass

    def from_proto(self):
        payload_type = Transaction.PayloadType("binary")
        #encoded_text = "CiCCVuSptT1oavBbf2UJfh+FHaOb15rhXgvMnyMPrpaLORIaGVfKCoAu9e0830glBZkJcmNoRXXOUbwvcz8aGhlXygqALvXtPN9IJQWZCXJjaEV1zlG8L3M/IhAAAAAAAAAAAAAAAAAAAAAKKAEwxbrg1gU6LAoGZGVwbG95EiJ7IlNvdXJjZVR5cGUiOiIxMSIsIlNvdXJjZSI6IjExMSJ9QGRKEAAAAAAAAAAAAAAAAAAATiBSEAAAAAAAAAAAAAAAAAAPQkBYAWJB5ZgDuJwK+EPpThEY0sAHc19immxH/LJCyXzj3OeaDUV7JGil7aIlcRTVsWAd32D5T12q9INlNVCT9m2lEV6/YgE="
        #encoded_text = "CiD/DXtAEjr1gTtq3T3pk2nL8CmkZPWzt7suFSPQhi4YEhIaGVeQ+6EMye7DjoRMJLuiXjJc1WRPcPmUV9IaGhlXkPuhDMnuw46ETCS7ol4yXNVkT3D5lFfSIhAAAAAAAAAAAA3gtrOnZAAAKAEw7O7m1gU6CAoGYmluYXJ5QOkHShAAAAAAAAAAAAAAAAAAD0JAUhAAAAAAAAAAAAAAAAAAAw1AWAFiQdX0esPCiDrfxGvCUt51UEZUaasdlYrcAkllPgyw6soeKq8+lRs1hYZPvYWDSzSWbhKs9D4xo5DgRbvdr5fRmekB"
        #encoded_text = "CiCCVuSptT1oavBbf2UJfh+FHaOb15rhXgvMnyMPrpaLORIaGVfKCoAu9e0830glBZkJcmNoRXXOUbwvcz8aGhlXygqALvXtPN9IJQWZCXJjaEV1zlG8L3M/IhAAAAAAAAAAAAAAAAAAAAAKKAEwxbrg1gU6LAoGZGVwbG95EiJ7IlNvdXJjZVR5cGUiOiIxMSIsIlNvdXJjZSI6IjExMSJ9QGRKEAAAAAAAAAAAAAAAAAAATiBSEAAAAAAAAAAAAAAAAAAPQkBYAWJB5ZgDuJwK+EPpThEY0sAHc19immxH/LJCyXzj3OeaDUV7JGil7aIlcRTVsWAd32D5T12q9INlNVCT9m2lEV6/YgE="
        encoded_text = "CiCd7cbbDYleNGNV8scCp6jkYpk/7hah7IhHsoUtSSRVZBIaGVcgewayZc0Og2LO7RuSi1alpXte7NOSLwsaGhlXIHsGsmXNDoNizu0bkotWpaV7XuzTki8LIhAAAAAAAAAAAA3gtrOnZAAAKAEwtsGb2AU6CAoGYmluYXJ5QOkHShAAAAAAAAAAAAAAAAAAD0JAUhAAAAAAAAAAAAAAAAAAAE4gWAFiQe4pGrSbpK0cWHSjhCvPAs4+lI6gk4KJg17qNTOUKXoWbYs6k8TRD/sRWjBGbESZ/TjiKIWG77Nvn7gzmTUNPOYA"
        transaction = Transaction("1","2","3","4","5", payload_type ,b'7',8, 9)
        transaction.from_proto(base64.decodebytes(bytes(encoded_text.encode("utf-8"))))
        '''
        org=transaction.get_hash()
        print(org)
        print(transaction.calculate_hash())
        print(transaction.calculate_hash() == org)
        print(transaction.get_sign())
        #transaction.sign()
        print(transaction.get_sign())
        '''
        str = transaction.to_proto()

        print("=============")

        for i in range(len(encoded_text)):
            if str[i] != encoded_text[i]:
                print("!=", i)
                print(encoded_text[i])
                print(str[i])

        print(str)
        print(encoded_text)
        #transaction.from_proto(base64.decodebytes(bytes(str.encode("utf-8"))))
        #print(bytes(encoded_text.encode("utf-8")))

        print(encoded_text == str)


if __name__ == '__main__':
    atest = transactiontest()
    atest.from_proto()
