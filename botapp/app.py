from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_halls():
    halls_data = {
        "halls": [
            {
                "id": 1,
                "names": ["SES", "First Hall"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture":'https://drive.google.com/uc?export=view&id=1Xgw0QKDORMmsma63jum2ofFrsg4FJXhB'
            },
            {
                "id": 2,
                "names": ["Achike", "Second Hall"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
               "picture" : "https://drive.google.com/uc?export=view&id=1Xgw0QKDORMmsma63jum2ofFrsg4FJXhB"
            },
            {
                "id": 3,
                "names": ["SBS", "Second Hall"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture" :"https://drive.google.com/uc?export=view&id=1wGyzHuf3zSfDEYapV7qiwpZBKa8gtS5A"
            },
            {
                "id": 4,
                "names": ["PT", "Printing Tech"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture" :"https://drive.google.com/uc?export=view&id=1XCMvHsie_mLaehxpdhnqM2d4tjsDkxon"
            },
            {
                "id": 5,
                "names": ["SCIT"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture" : "https://drive.google.com/uc?export=view&id=1V5tqdjft7sl4VFpxOU_QeQ1Ps2Wl19JR"
            },
            {
                "id": 6,
                "names": ["Okata", "Second Hall"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture": "https://drive.google.com/uc?export=view&id=1yTd50fBjxYCvLPRBv07sUbyfq2jN-2_R"
            },
            {
                "id": 7,
                "names": ["LIS", "Library & Info. secience"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture": "https://drive.google.com/uc?export=view&id=1LOoLP-B1BcQU-9vgQicc8ViqsGavNZEW"
            },
            {
                "id": 8,
                "names": ["Food tech", "FT Main", "FT 2","FT up"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture": "https://drive.google.com/uc?export=view&id=1hyURY3DuydFxhZqPKzb59B_JprXnN71S"
            },
            {
                "id": 9,
                "names": ["CS", "Computer Science"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture": "https://drive.google.com/uc?export=view&id=1Lf6NfCr4z6QZPUoR8r6Bhm57wzOqpgXi"
            },
            {
                "id": 10,
                "names": ["EE", "Electrical Electronice"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture": "https://drive.google.com/uc?export=view&id=1FgxqU1RhB6wlfKA4Thi1m78YvJcA8mp4"
            },
            {
                "id": 11,
                "names": ["A wing", "B wing","C wing"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture": "https://drive.google.com/uc?export=view&id=1yadN413iGMmqFxRyY8dxePYQC2eg9geh"
            },
            {
                "id": 12,
                "names": ["UMC", "Utra Morden Class Room"],
                "coordinates": {"latitude": 37.7749, "longitude": -122.4194},
                "picture": "https://drive.google.com/uc?export=view&id=14qrwoQecej7SYINxBR0ngut3HzX4U1EY"
            }
        ]
    }
    return jsonify(halls_data)

if __name__ == '__main__':
    app.run(debug=True)

