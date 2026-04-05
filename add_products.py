from Website import create_app, db
from Website.models import Product

app = create_app()

# Sample keyboard products
keyboards = [
    {
        'product_code': 'KEYGEN0011',
        'name': 'DESKTOP KEYBOARD - GENIUS K220 SCORPION',
        'category': 'keyboards',
        'description': 'Wired membrane gaming keyboard with quiet and responsive keys. RGB multi-color backlighting with customizable lighting effects. 19-key rollover and anti-ghosting support for precise input.',
        'price': 14000.00,
        'stock': 3,
        'image_url': '/static/44357_2618_THERMALTAKE-TT-PREMIUM-X1-RGB-KB-TPX-BLBRUS-01-copy.png',
        'warranty': '1 year warranty',
        'in_stock': True
    },
    {
        'product_code': 'KEYGEN0012',
        'name': 'KEYBOARD - RAPOO V500 ALLOY MECHANICAL GAMING KEYBOARD',
        'category': 'keyboards',
        'description': 'Premium mechanical gaming keyboard with aluminum alloy construction. Durable switches with customizable RGB lighting. Perfect for gaming and typing.',
        'price': 14000.00,
        'stock': 5,
        'image_url': '/static/20241009113121_1.jpg',
        'warranty': '3 year warranty',
        'in_stock': True
    }
]

# Sample mouse products
mice = [
    {
        'product_code': 'MOUSEGEN0011',
        'name': 'ASUS P306 TUF GAMING M4 WIRELESS MOUSE',
        'category': 'mice',
        'description': 'Wireless gaming mouse with precision tracking and low latency. Ergonomic design with programmable buttons for gaming.',
        'price': 12000.00,
        'stock': 8,
        'image_url': '/static/asus_mouse.png',
        'warranty': '1 year warranty',
        'in_stock': True
    }
]

# Sample headset products
headsets = [
    {
        'product_code': 'HEADGEN0011',
        'name': 'GAMING HEADSET - CORSAIR HS50 PRO',
        'category': 'headsets',
        'description': 'Professional gaming headset with 7.1 surround sound. Noise-cancelling microphone and comfortable ear cups for long gaming sessions.',
        'price': 18000.00,
        'stock': 4,
        'image_url': '/static/corsair_headset.png',
        'warranty': '2 year warranty',
        'in_stock': True
    }
]

all_products = keyboards + mice + headsets

with app.app_context():
    try:
        # Check if products already exist to avoid duplicates
        for product_data in all_products:
            existing = Product.query.filter_by(
                product_code=product_data['product_code']).first()
            if not existing:
                product = Product(**product_data)
                db.session.add(product)
                print(f"Added: {product_data['name']}")
            else:
                print(f"Skipped (already exists): {product_data['name']}")

        db.session.commit()
        print("\n✓ All products added successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
