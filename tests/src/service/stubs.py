stub_artist_validated = {
    "artist_id": 12345,
    "cache": True,
}

stub_dynamodb_item = {'transaction_id': '3ff8f689-78cc-413c-9104-7376db096368', 'artist_name': 'Luis Fonsi & Daddy Yankee', 'artist_id': 12345}

stub_songs_treated_template = {
    "top_ten_songs": [
        {
            "artist_name": "Justin Bieber",
            "title": "Despacito (Remix)",
            "full_title": "Despacito (Remix) by Luis Fonsi & Daddy Yankee (Ft. Justin Bieber)",
            "url_song": "https://genius.com/Luis-fonsi-and-daddy-yankee-despacito-remix-lyrics",
            "release_date": "April 17, 2017",
            "song_art_image_url": "https://images.genius.com/4164dff756ddd455675789bd67fe5f1a.1000x1000x1.png"
        },
        {
            "artist_name": "Justin Bieber",
            "title": "I’m the One",
            "full_title": "I'm the One by DJ Khaled (Ft. Chance the Rapper, Justin Bieber, Lil Wayne & Quavo)",
            "url_song": "https://genius.com/Dj-khaled-im-the-one-lyrics",
            "release_date": "April 28, 2017",
            "song_art_image_url": "https://images.genius.com/6127733e5dbc43f75fcbf1b92e48a068.1000x1000x1.png"
        },
    ]
}

stub_songs_result_genius = {
    "response": {
        "songs": [
            {
                "annotation_count": 11,
                "api_path": "/songs/3057010",
                "artist_names": "Luis Fonsi & Daddy Yankee (Ft. Justin Bieber)",
                "full_title": "Despacito (Remix) by Luis Fonsi & Daddy Yankee (Ft. Justin Bieber)",
                "header_image_thumbnail_url": "https://images.genius.com/93e9e3fa0ab18bc4613d385f287090c6.300x300x1.jpg",
                "header_image_url": "https://images.genius.com/93e9e3fa0ab18bc4613d385f287090c6.1000x1000x1.jpg",
                "id": 3057010,
                "lyrics_owner_id": 104344,
                "lyrics_state": "complete",
                "path": "/Luis-fonsi-and-daddy-yankee-despacito-remix-lyrics",
                "pyongs_count": 409,
                "relationships_index_url": "https://genius.com/Luis-fonsi-and-daddy-yankee-despacito-remix-sample",
                "release_date_components": {
                    "year": 2017,
                    "month": 4,
                    "day": 17
                },
                "release_date_for_display": "April 17, 2017",
                "song_art_image_thumbnail_url": "https://images.genius.com/4164dff756ddd455675789bd67fe5f1a.300x300x1.png",
                "song_art_image_url": "https://images.genius.com/4164dff756ddd455675789bd67fe5f1a.1000x1000x1.png",
                "stats": {
                    "unreviewed_annotations": 0,
                    "hot": False,
                    "pageviews": 23391019
                },
                "title": "Despacito (Remix)",
                "title_with_featured": "Despacito (Remix) (Ft. Justin Bieber)",
                "url": "https://genius.com/Luis-fonsi-and-daddy-yankee-despacito-remix-lyrics",
                "featured_artists": [
                    {
                        "api_path": "/artists/357",
                        "header_image_url": "https://images.genius.com/be2c60bdfb3ea6844a46cc5873c75b89.1000x563x1.jpg",
                        "id": 357,
                        "image_url": "https://images.genius.com/8c95afb142e16e2e053b4384514dc339.938x938x1.png",
                        "is_meme_verified": False,
                        "is_verified": True,
                        "name": "Justin Bieber",
                        "url": "https://genius.com/artists/Justin-bieber",
                        "iq": 1533
                    }
                ],
                "primary_artist": {
                    "api_path": "/artists/1119780",
                    "header_image_url": "https://images.genius.com/be123903c448d5f64ddac6476dc50aa4.847x476x1.jpg",
                    "id": 1119780,
                    "image_url": "https://images.genius.com/365d323e22c93fe869478efde436d233.393x393x1.jpg",
                    "is_meme_verified": False,
                    "is_verified": False,
                    "name": "Luis Fonsi & Daddy Yankee",
                    "url": "https://genius.com/artists/Luis-fonsi-and-daddy-yankee"
                }
            },
            {
                "annotation_count": 26,
                "api_path": "/songs/3004837",
                "artist_names": "DJ Khaled (Ft. Chance the Rapper, Justin Bieber, Lil Wayne & Quavo)",
                "full_title": "I'm the One by DJ Khaled (Ft. Chance the Rapper, Justin Bieber, Lil Wayne & Quavo)",
                "header_image_thumbnail_url": "https://images.genius.com/9e1b48313ac3c4b8a96fa666962384d3.300x300x1.jpg",
                "header_image_url": "https://images.genius.com/9e1b48313ac3c4b8a96fa666962384d3.1000x1000x1.jpg",
                "id": 3004837,
                "lyrics_owner_id": 3344750,
                "lyrics_state": "complete",
                "path": "/Dj-khaled-im-the-one-lyrics",
                "pyongs_count": 190,
                "relationships_index_url": "https://genius.com/Dj-khaled-im-the-one-sample",
                "release_date_components": {
                    "year": 2017,
                    "month": 4,
                    "day": 28
                },
                "release_date_for_display": "April 28, 2017",
                "song_art_image_thumbnail_url": "https://images.genius.com/6127733e5dbc43f75fcbf1b92e48a068.300x300x1.png",
                "song_art_image_url": "https://images.genius.com/6127733e5dbc43f75fcbf1b92e48a068.1000x1000x1.png",
                "stats": {
                    "unreviewed_annotations": 0,
                    "hot": False,
                    "pageviews": 5434514
                },
                "title": "I’m the One",
                "title_with_featured": "I'm the One (Ft. Chance the Rapper, Justin Bieber, Lil Wayne & Quavo)",
                "url": "https://genius.com/Dj-khaled-im-the-one-lyrics",
                "featured_artists": [
                    {
                        "api_path": "/artists/4",
                        "header_image_url": "https://images.genius.com/3b3485a28f2eb47c5ff3d7691e71bcba.1000x333x1.jpg",
                        "id": 4,
                        "image_url": "https://images.genius.com/aa8b9dce2492fe413c23f77b643788fd.914x914x1.jpg",
                        "is_meme_verified": True,
                        "is_verified": True,
                        "name": "Lil Wayne",
                        "url": "https://genius.com/artists/Lil-wayne",
                        "iq": 4605
                    },
                    {
                        "api_path": "/artists/16751",
                        "header_image_url": "https://images.genius.com/27ac36b6f8cdba29f97d0a94834bbdb7.1000x563x1.jpg",
                        "id": 16751,
                        "image_url": "https://images.genius.com/9db1a9643a028d62543e44c90da3a6ad.1000x1000x1.jpg",
                        "is_meme_verified": False,
                        "is_verified": True,
                        "name": "Chance the Rapper",
                        "url": "https://genius.com/artists/Chance-the-rapper",
                        "iq": 48638
                    },
                    {
                        "api_path": "/artists/61600",
                        "header_image_url": "https://images.genius.com/cfd25c6603c03d1810a63e65506d7413.1000x563x1.png",
                        "id": 61600,
                        "image_url": "https://images.genius.com/ff947bf0574f3cb16bc418078b7bf191.1000x1000x1.png",
                        "is_meme_verified": False,
                        "is_verified": False,
                        "name": "Quavo",
                        "url": "https://genius.com/artists/Quavo"
                    },
                    {
                        "api_path": "/artists/357",
                        "header_image_url": "https://images.genius.com/be2c60bdfb3ea6844a46cc5873c75b89.1000x563x1.jpg",
                        "id": 357,
                        "image_url": "https://images.genius.com/8c95afb142e16e2e053b4384514dc339.938x938x1.png",
                        "is_meme_verified": False,
                        "is_verified": True,
                        "name": "Justin Bieber",
                        "url": "https://genius.com/artists/Justin-bieber",
                        "iq": 1533
                    }
                ],
                "primary_artist": {
                    "api_path": "/artists/158",
                    "header_image_url": "https://images.genius.com/ab6d177ad39383915733cf37ca1fb301.999x999x1.jpg",
                    "id": 158,
                    "image_url": "https://images.genius.com/ab6d177ad39383915733cf37ca1fb301.999x999x1.jpg",
                    "is_meme_verified": True,
                    "is_verified": True,
                    "name": "DJ Khaled",
                    "url": "https://genius.com/artists/Dj-khaled",
                    "iq": 5181
                }
            }
        ],
        "next_page": 2
    }
}
