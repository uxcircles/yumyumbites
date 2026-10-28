# Menu data, transcribed from the two menu PDFs on the old site (assets/menus/).
# Diet marks: "vg" = vegan (marked on the printed menu), "v" = vegetarian, "vgo" = vegan option.
# Edit prices here, then run:  python3 _build/build.py

MENU = [
    {
        "id": "fan-tuan", "en": "Fan Tuan", "zh": "臺式飯糰",
        "note": "Taiwanese rice roll, wrapped to go. With egg, gherkins, fried mustard, flakes, cucumber and our homemade vegan mayo.",
        "items": [
            ("Chicken", "雞肉", "6.00", ""),
            ("Tuna", "鮪魚", "6.20", ""),
            ("Prawn", "鮮蝦", "6.50", ""),
            ("Falafel", "鷹嘴豆丸子", "6.20", "vg"),
            ("Veg", "蔬菜", "5.80", "vg"),
            ("Meatball", "小肉丸", "6.00", ""),
        ],
    },
    {
        "id": "fried", "en": "Yummy Selection", "zh": "人氣炸物",
        "note": "Night-market fried favourites.",
        "items": [
            ("Da Ji Pai", "大雞排", "7.29", "", "Boneless Taiwanese fried chicken, the size of your face."),
            ("Supreme Chicken Burger", "元氣香雞堡", "7.29", ""),
            ("Popcorn Chicken", "夜市鹽酥雞", "7.29", "", "Yum Yum Bites special, spicy chilli or plum."),
            ("Korean Fried Chicken", "韓式炸雞塊", "7.29", ""),
            ("Yum Yum Box", "甲奔炸物盒", "7.29", "vgo", "Chicken, handmade fish tempura, meatballs, tofu, beans and curly fries."),
        ],
    },
    {
        "id": "bento", "en": "Classic Bento", "zh": "經典便當",
        "note": "Served with rice, mixed veg, pickled cabbage and a tea-braised egg.",
        "items": [
            ("Fried Chicken Bento", "經典雞排便當", "10.90", ""),
            ("Korean Fried Chicken Bento", "韓式雞排便當", "11.70", ""),
            ("Korean Fried Tofu Bento", "韓式炸豆腐便當", "11.70", "vg"),
            ("Braised Pork Belly Bento", "滷肉飯便當", "11.00", ""),
        ],
    },
    {
        "id": "rice-noodle", "en": "Rice & Noodles", "zh": "飽足飯麵",
        "note": "",
        "items": [
            ("Spicy Braised Beef Brisket Rice", "香辣牛腩飯", "11.00", ""),
            ("Japanese Curry Chicken Rice", "咖哩雞排飯", "11.30", ""),
            ("Japanese Curry Tofu Rice", "咖哩豆腐飯", "11.30", "v"),
            ("Spicy Braised Beef Brisket Noodle", "香辣牛腩麵", "11.90", ""),
            ("Spicy Seafood Noodle", "香辣海鮮麵", "12.90", ""),
        ],
    },
    {
        "id": "snacks", "en": "Appetisers & Sides", "zh": "小吃炸物",
        "note": "",
        "items": [
            ("Taiwanese Fried Tofu", "臺式炸豆腐", "5.90", ""),
            ("Korean Fried Tofu", "韓式炸豆腐", "5.90", "vg"),
            ("Golden Fried Egg (2)", "金黃香酥蛋", "3.99", ""),
            ("Spring Onion Pancake", "蔥油餅蛋", "2.99", "", "Or two for £5.50."),
            ("Toastie", "烤吐司", "2.60", "", "Jam, peanut butter, Nutella, cheese or butter. Two for £4.50."),
            ("Meatballs with Sauce (10 / 15)", "小肉丸配醬", "6.20 / 8.50", ""),
            ("Curly Fries", "捲捲薯條", "3.90", "vg"),
            ("Fries (reg / large)", "薯條", "2.90 / 3.90", "vg"),
            ("Onion Rings (8)", "洋蔥圈", "3.90", "vg"),
            ("Hash Browns (2)", "薯餅", "1.99", "vg"),
            ("Tea Braised Egg", "茶香滷蛋", "1.99", "v"),
        ],
    },
    {
        "id": "drinks", "en": "Bubble Tea & Drinks", "zh": "特調飲品",
        "note": "",
        "items": [
            ("Classic Bubble Tea / Milk Tea", "經典珍珠奶茶", "4.80", ""),
            ("Thai Bubble Tea / Milk Tea", "泰式珍珠奶茶", "5.20", "vg"),
            ("Winter Melon Drink", "古早味冬瓜茶", "5.20", "vg"),
            ("Soya Drink, Original", "原味豆漿", "3.20", "vg"),
            ("Soya Drink, Caramel / Strawberry / Chocolate", "風味豆漿", "3.80", "vg"),
            ("Man Tou, Sweet Fried Bun", "炸饅頭", "6.50", "v", "Original, black choc, white choc, Biscoff, Oreo or cheesy."),
        ],
    },
]
