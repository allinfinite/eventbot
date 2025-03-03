# Telegram Event Bot + Marketplace for Cloudron

This project provides a Telegram bot that:

- Detects events across all topics using **NLP-based classification**.
- Detects offers/requests in a dedicated marketplace topic using **NLP-based classification**.
- Automatically adds events to a **public Google Calendar**.
- Exposes a **public website** on Cloudron that:
    - Displays the Google Calendar (embedded).
    - Displays and filters the marketplace offers & requests.
- Includes a training script to fine-tune your own NLP models.

## Features

- Google Calendar Integration (for public events).
- OCR support (Google Vision or Tesseract) for extracting text from flyers.
- NLP classification for both events and marketplace messages.
- Custom filters for viewing offers/requests by type or user.
- Mobile-friendly design.

## Deployment

- Fully Cloudron-compatible with Dockerfile & CloudronManifest.json.
- Easy to redeploy and update.

## Folder Structure

```
eventbot/
├── bot.py                # Telegram bot
├── web_server.py         # Flask server for marketplace.json & public site
├── templates/
│   └── index.html        # Public website (calendar + marketplace with filters)
├── static/
│   └── style.css         # CSS for website styling
├── models/
│   ├── event_classifier.pkl     # Pre-trained model for event detection
│   ├── marketplace_classifier.pkl # Pre-trained model for offers/requests
├── data/
│   └── marketplace.json  # Offers/requests data file (persisted across restarts)
├── Dockerfile             # For Cloudron deployment
├── CloudronManifest.json  # Cloudron config
├── start.sh               # Launch bot & web server together
├── requirements.txt       # Python dependencies
├── train_model.py         # Training script for NLP models
└── README.md
```

## License

MIT