import random
from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def browse(request):
    from shop.models import Product
    from services.models import ServicePackage

    products = Product.objects.filter(is_active=True).order_by('-created_at')
    services = ServicePackage.objects.filter(is_active=True).order_by('name')

    return render(
        request,
        'home/browse.html',
        {
            'products': products,
            'services': services,
        }
    )


def ai_photos(request):
    from shop.models import Product
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'home/ai_photos.html', {'products': products})


def ai_bundles(request):
    prompts = [
        "Cinematic portrait, golden hour rim light, 85mm lens, shallow depth of field, soft bokeh",
        "Editorial studio headshot, Rembrandt lighting, charcoal backdrop, sharp focus",
        "Moody cyberpunk alley, neon pink and teal, reflective puddles, rain-speckled jacket",
        "Clean corporate headshot, soft key light, blurred office background, confident smile",
        "Fantasy elf archer, forest clearing, dappled light, ornate leather armor",
        "Baroque oil painting style, dramatic chiaroscuro, ornate frame, regal pose",
        "Minimalist black-and-white portrait, high contrast, grainy film look",
        "Vibrant street fashion, wide angle, urban graffiti wall, motion blur",
        "Retro 80s synthwave, magenta and cyan grid, chrome text, palm silhouettes",
        "Astronaut helmet reflection, earthrise, cinematic lighting, crisp visor detail",
        "Painterly watercolor portrait, pastel palette, soft edges, handmade paper",
        "Product mockup, matte black bottle, softbox lighting, seamless background",
        "Desert wanderer, flowing cloak, sandstorm, low sun silhouette",
        "Nordic landscape, fjord at dawn, misty mountains, calm water reflection",
        "Architectural brutalism, overcast sky, concrete textures, wide composition",
        "Lux jewelry macro shot, shallow depth, dark velvet backdrop, sparkle highlights",
        "Noir detective scene, rain-soaked street, trench coat, cigarette glow",
        "Anime hero pose, dynamic speed lines, vibrant cel shading, dramatic sky",
        "Studio beauty closeup, glossy skin, colored gels, crisp catchlights",
        "Vintage film still, 35mm grain, muted colors, candid expression",
        "Pastel kawaii cafe, cozy interior, latte art, soft morning light",
        "Futuristic UI dashboard, holographic overlays, deep blues, clean lines",
        "Luxury interior, marble surfaces, warm accent lighting, wide shot",
        "Action freeze-frame, flying debris, high shutter speed, sharp subject",
        "Ghibli-inspired countryside, lush greens, winding path, warm sunlight",
        "Editorial fitness shoot, dramatic rim light, chalk dust in air",
        "Surreal double exposure, forest overlay on portrait, soft blending",
        "Moody musician portrait, backlit haze, lens flare, stage lights",
        "Desaturated war photo, gritty textures, dramatic clouds, worn uniform",
        "High-fashion runway, long lens compression, spotlight, bold outfit",
        "Cozy reading nook, warm lamp glow, rain on window, shallow depth",
        "Drone shot of coastline, turquoise water, white foam patterns, high contrast",
        "Macro leaf details, dewdrops, translucent veins, backlit",
        "Afrofuturism portrait, metallic face paint, neon accents, dark background",
        "Painterly renaissance portrait, rich fabrics, chiaroscuro lighting",
        "Minimal product flat lay, pastel backdrop, balanced composition",
        "Cybernetic enhancements, close-up portrait, glowy implants, cool palette",
        "Retro polaroid style, soft flash, instant film border, candid moment",
        "Street food stall at night, steam, colorful signage, shallow depth",
        "Epic mountain sunrise, god rays, low clouds, hiker silhouette",
        "Studio sneaker shot, floating effect, light painting trails",
        "Moody library scene, dust motes, window light, vintage tones",
        "Sunset beach silhouette, long exposure water blur, warm tones",
        "Comic book cover, bold ink lines, halftone shading, dynamic pose",
        "Luxury watch macro, sapphire crystal reflections, dark gradient background",
        "Nordic minimal living room, neutral palette, soft daylight",
        "Mystical foggy forest, volumetric light, tall pines, path leading inward",
        "Color splash portrait, monochrome with vibrant accent, sharp eyes",
        "Old master oil painting, cracked varnish texture, muted palette",
        "Vaporwave collage, statues, Japanese text, glitch grain",
        "Harsh desert sunlight portrait, high contrast, rim-lit dust",
        "Editorial food shot, rustic table, directional side light, steam rising",
        "Tech product render, isometric view, soft shadows, clean background",
        "Glamour portrait, beauty dish lighting, glossy lips, bokeh backdrop",
        "Sci-fi corridor, volumetric light beams, reflective floor, lone figure",
        "Romantic candlelit dinner, shallow depth, warm bokeh, intimate framing",
        "Arctic explorer, snow particles, frost on clothing, overcast light",
        "Steampunk inventor, brass gadgets, workshop setting, dramatic light",
        "Underwater scene, sunrays through water, divers, particulate haze",
        "High-key fashion, pure white background, crisp shadows, colorful outfit",
        "Moody cocktail shot, bar backlight, condensation, citrus twist",
        "Soft newborn portrait, natural window light, neutral blanket",
        "Sports action, frozen sweat, stadium lights, intense expression",
        "Cinematic car ad, rain on hood, city lights reflections, low angle",
        "Fantasy castle on cliff, clouds below, warm sunset, epic scale",
        "Tattoo studio portrait, rim light, dark backdrop, ink focus",
        "Monochrome architectural lines, strong symmetry, deep blacks",
        "Festival night, colorful lights, shallow depth, candid energy",
        "Art deco poster, geometric shapes, gold accents, bold typography",
        "Gothic cathedral interior, stained glass glow, wide dynamic range",
        "Organic skincare flat lay, linen cloth, soft daylight, natural props",
        "Wildlife close-up, shallow depth, catchlight in eyes, detailed fur",
        "Pastel cityscape, dawn haze, soft gradients, dreamy mood",
        "Long exposure city lights, light trails, crisp skyline",
        "Caribbean beach aerial, sandbar patterns, crystal water, high saturation",
        "Fine art nude silhouette, rim light, monochrome, minimal",
        "Moody gamer setup, RGB lighting, ultrawide monitor, shallow depth",
        "Bold typographic poster, high contrast, minimal palette",
        "Portrait with floral crown, soft pastel tones, diffused light",
        "Winter cabin night, warm interior glow, snowy pines, starry sky",
        "Industrial factory, shafts of light, dust particles, dramatic scale",
        "Surf action shot, frozen splash, telephoto compression, bright tones",
        "Classic film noir couple, cigarette smoke, blinds shadow, monochrome",
        "Travel journal flat lay, map, camera, notebook, natural light",
        "Desert night sky, Milky Way arch, foreground cactus, long exposure",
        "Chef plating dish, steam rising, side light, shallow depth",
        "Aerial farmland patterns, golden hour, leading lines, patchwork fields",
        "Portrait with colored gels, split lighting magenta/cyan, crisp focus",
        "Vintage motorcycle, low angle, dusty road, sunset glow",
        "Minimal still life, single object, dramatic shadow, solid backdrop",
        "Cosplay hero shot, studio backdrop, rim light, smoke machine",
        "Pet portrait, natural window light, sharp eyes, neutral background",
        "Luxury spa scene, soft towels, candles, shallow depth, warm tones",
        "Dramatic orchestra shot, conductor motion blur, spotlight beams",
        "Macro coffee beans, shallow depth, rich browns, texture focus",
        "Neon portrait, edge lighting, reflective jacket, rainy backdrop",
        "Classic painterly landscape, oil texture, warm sunlight, rolling hills",
        "Tech keynote stage, presenter silhouette, big screen glow, wide shot",
        "Minimal line art poster, black on off-white, bold composition",
        "Night city alley, puddle reflections, cinematic grading, moody",
        "Portrait with prism refraction, rainbow shards, dreamy focus",
        "Editorial magazine cover, bold masthead space, confident pose",
        "Stylized low poly landscape, pastel colors, soft lighting",
        "Luxury perfume ad, glass bottle splash, high-speed flash, dark background",
        "Soft morning bedroom, linen sheets, window light, airy mood",
        "Concept car render, studio lighting, glossy paint, dramatic shadows",
    ]
    shuffled = prompts[:]
    random.shuffle(shuffled)
    bundle_options = [
        {"label": "Products", "description": "Ready-made portrait packs", "count": "Shop", "url_name": "product_list"},
        {"label": "100 Prompts", "description": "Full prompt vault (randomized)", "count": 100},
        {"label": "50 Prompts", "description": "Half vault selection", "count": 50},
        {"label": "10 Prompts", "description": "Curated starter set", "count": 10},
        {"label": "5 Prompts", "description": "Quick inspiration pack", "count": 5},
    ]
    return render(request, 'home/bundles.html', {
        'prompts': shuffled,
        'bundle_options': bundle_options,
    })
