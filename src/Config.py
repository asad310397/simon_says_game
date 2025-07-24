Config = {
    "game": {
        "caption": "Simon Says",
        "width": 800,
        "height": 600,
        "fps": 30,
        "font-size": 20,
        "font": "../assets/PressStart2P-Regular.ttf",
        "color-delay": 20,
        "turn-delay": 40,
    },
    "squares": {
        "red": {
            "color": [255, 0, 0, 180],
            "position": (10, 40, 390, 270),
            "note": "../assets/fa.mp3",
        },
        "yellow": {
            "color": [255, 255, 0, 180],
            "position": (10, 320, 390, 270),
            "note": "../assets/re.mp3",
        },
        "blue": {
            "color": [0, 0, 255, 180],
            "position": (410, 40, 380, 270),
            "note": "../assets/si.mp3",
        },
        "green": {
            "color": [0, 255, 0, 180],
            "position": (410, 320, 380, 270),
            "note": "../assets/sol.mp3",
        },
    },
    "colors": {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
    },
}
