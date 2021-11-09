# Bing Web Scraper

A Bing web scraper with an API.

## Installation

```bash
git clone https://github.com/arturnawrot/web-scraper.git && cd web-scraper
pip install -r requirements.txt
python3 server.py
```
## Docker

```bash
docker build --no-cache -t scraper .
docker run -p 5000:5000 scraper
```

## Example usage

```bash
curl -X GET "http://localhost:5000/?query=Apple"
```

## Response

```
[
    {
        "description": "Apple Footer. 1. $4.99/month after free trial. One subscription per Family Sharing group. Offer good for 3 months after eligible device activation. Plan 
automatically renews until canceled. Restrictions and other terms apply. Apple TV+ is $4.99/month after free trial. One subscription per Family Sharing group.",
        "title": [],
        "url": "https://www.apple.com/"
    },
    {
        "description": "Apple TV+ is included for 3 months when you purchase an Apple device and redeem the offer within 90 days. 1. Check eligibility. Free 7-day trial. $4.99/mo. A monthly subscription is just $4.99 per month after a free 7-day trial. Share Apple TV+ with your family. 2. Try it free. Free 1\u2011month trial. Apple One.",
        "title": " TV+ - ",
        "url": "https://www.apple.com/apple-tv-plus/"
    },
    {
        "description": "Your Apple ID is the account you use for all Apple services.",
        "title": "Manage your ",
        "url": "https://appleid.apple.com/#!&page=signin"
    },
    {
        "description": "Apple Store. Consumer Electronics Computer & Equipment Dealers Computers & Computer Equipment-Service & Repair. Website. (206) 892-0433. 2651 NE 49th St. Seattle, WA 98105. From Business: Visit the University Village Apple Retail Store to shop for Mac, iPhone, iPad, iPod, and more.",
        "title": " Store Locations & Hours Near Redmond, WA - YP.com",
        "url": "https://www.yellowpages.com/redmond-wa/apple-store"
    },
    {
        "description": "Find Apple Retail Stores, iPhone and iPad Stores in your Area - All States, all Cities.",
        "title": " Macintosh and iPhone Stores in Redmond, WA",
        "url": "http://apple-store.in/98052-redmond/"
    },
    {
        "description": "Apple Bellevue Square. Open until 9:00 p.m. We\u2019re open and look forward to welcoming you. Shop by walking in, reserving a one-on-one session with a 
Specialist or buy online and pickup in store. Get support at the Genius Bar in store or by making a reservation. Face masks required. If you need one, just ask.",
        "title": " -   Store - ",
        "url": "https://www.apple.com/retail/bellevuesquare/"
    },
    {
        "description": "Sign in to iCloud to access your photos, videos, documents, notes, contacts, and more. Use your Apple ID or create a new account to start using Apple services.",
        "title": "iCloud",
        "url": "https://www.icloud.com/"
    },
    {
        "description": "7425 166th Ave NE. Suite C115. Redmond, WA 98052 (425) 885-4783",
        "title": "Mac &   Product Reseller in  , Washington ...",
        "url": "https://store.simplymac.com/pages/redmond-wa"
    },
    {
        "description": "3 Apple Watch Series 7 has a water resistance rating of 50 meters under ISO standard 22810:2010. This means that they may be used for shallow-water activities like swimming in a pool or ocean. However, they should not be used for scuba diving, waterskiing, or other activities involving high-velocity water or submersion below shallow depth.",
        "title": " Watch Series 7 Near Me,   Watch Redmond ...",
        "url": "https://www.att.com/stores/washington/redmond/apple-watch"
    },
    {
        "description": "Our specialty is caramel apple, but we also do pretzel knots as party favors. All of our products are made to order so you can be sure you will be enjoying fresh, locally grown, decadent treats. Due to the delicateness of our party favors, we only service locally in the Metropolitan Seattle area.",
        "title": "Caramel Apples & Party Favors in Seattle - Deliciously Reds",
        "url": "http://deliciouslyreds.com/"
    }
```
