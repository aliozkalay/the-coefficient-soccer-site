import os
OUT=os.path.dirname(os.path.abspath(__file__))  # writes pages next to this script
DOM='https://thecoefficiency.com'
CH='https://www.youtube.com/channel/UCUXaoWNWGINNavIVrNACiBQ'
SUB=CH+'?sub_confirmation=1'
HANDLE='https://www.youtube.com/@TheCoefficient-g8c'
UPLOADS='UUUXaoWNWGINNavIVrNACiBQ'  # channel ID with UC -> UU = auto "latest uploads" playlist
EMAIL='info@thecoefficiency.com'
TAG='European football, explained with data.'
YT='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.2 3.6-6.2 3.6z"/></svg>'
NAV=[('index.html','Home'),('videos.html','Videos'),('about.html','About'),('contact.html','Contact')]

def page(fn,title,desc,body,path=None):
    path = '/' if fn=='index.html' else '/'+fn
    nav=''.join(f'<li><a class="link" href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    full = f'The Coefficient | {title}' if fn!='index.html' else 'The Coefficient | European football, explained with data'
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#041030">
<link rel="canonical" href="{DOM}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The Coefficient">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOM}{path}">
<meta property="og:image" content="{DOM}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/css/style.css">
<script src="/assets/js/main.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="/"><img src="/assets/img/icon-192.png" alt="" width="40" height="40">The Coefficient</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
    <ul id="menu">{nav}<li><a class="btn btn-sub" href="{SUB}" target="_blank" rel="noopener">{YT}Subscribe</a></li></ul>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot">
    <div>
      <strong style="font-family:var(--f-title);font-style:italic;text-transform:uppercase;font-size:1.2rem;color:#fff">The Coefficient</strong><br>
      {TAG} Educational analysis only. No gambling content.<br>
      &copy; <span data-year>2026</span> The Coefficient. All graphics original.
    </div>
    <nav aria-label="Footer"><a href="/videos.html">Videos</a><a href="/about.html">About</a><a href="/contact.html">Contact</a><a href="{HANDLE}" target="_blank" rel="noopener">YouTube</a></nav>
  </div>
</footer>
</body>
</html>
'''
    open(os.path.join(OUT,fn),'w').write(html)

subband=f'''<section><div class="wrap"><div class="band">
  <div><h2>Learn to see the game differently</h2><p>New Shorts every morning on YouTube.</p></div>
  <a class="btn btn-sub" href="{SUB}" target="_blank" rel="noopener">{YT}Subscribe on YouTube</a>
</div></div></section>'''

pillars=f'''<div class="grid g4">
  <div class="card accent"><span class="num">01</span><h3>Daily Shorts</h3><p>One tactical idea or stat, explained in under a minute.</p></div>
  <div class="card accent"><span class="num">02</span><h3>Match Previews</h3><p>Data-driven looks at the biggest European games. For learning, not betting.</p></div>
  <div class="card accent"><span class="num">03</span><h3>Club Tier Rankings</h3><p>Level 1 to 5, based on squad, organization and structure.</p></div>
  <div class="card accent"><span class="num">04</span><h3>How to Read a Game</h3><p>Lessons for players, parents, coaches and young fans.</p></div>
</div>'''

# ---------- HOME ----------
page('index.html','Home','The Coefficient: European football, explained with data. Formations, pressing, build-up patterns, xG and the numbers behind every result.',f'''
<section class="hero"><div class="wrap">
  <img class="logo" src="/assets/img/logo-512.png" alt="The Coefficient logo" width="150" height="150">
  <p class="kicker">Data. Tactics. European Football.</p>
  <h1>The Coefficient</h1>
  <div class="rule"></div>
  <p class="lead">{TAG} Formations, pressing, build-up patterns, xG and the numbers behind every result, broken down the way a coach and an analyst see the game.</p>
  <div class="cta-row">
    <a class="btn btn-sub" href="{SUB}" target="_blank" rel="noopener">{YT}Subscribe on YouTube</a>
    <a class="btn btn-ghost" href="/videos.html">Watch the videos</a>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Every week</span><h2>What you'll get</h2></div></div>
  {pillars}
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="section-head">
    <div><span class="eyebrow">On the channel</span><h2>Latest Shorts</h2></div>
    <a class="btn btn-ghost" href="{CH}/shorts" target="_blank" rel="noopener">All Shorts on YouTube</a>
  </div>
  <!-- PLACEHOLDERS: swap each card for a real Short once published, e.g.
       <div class="short"><iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="..." loading="lazy" allowfullscreen></iframe></div> -->
  <div class="grid g4">
    <a class="short ph" href="{CH}/shorts" target="_blank" rel="noopener" style="background-image:url(/assets/img/logo-card-9x16.jpg)"><span class="tag soon">Planned</span><strong>Totals vs. per-game stats</strong><small>How to read stats: why goals per game matters more than a total.</small></a>
    <a class="short ph" href="{CH}/shorts" target="_blank" rel="noopener" style="background-image:url(/assets/img/logo-card-9x16.jpg)"><span class="tag">Short</span><strong><span class="todo">[Short title]</span></strong><small>Add once published.</small></a>
    <a class="short ph" href="{CH}/shorts" target="_blank" rel="noopener" style="background-image:url(/assets/img/logo-card-9x16.jpg)"><span class="tag">Short</span><strong><span class="todo">[Short title]</span></strong><small>Add once published.</small></a>
    <a class="short ph" href="{CH}/shorts" target="_blank" rel="noopener" style="background-image:url(/assets/img/logo-card-9x16.jpg)"><span class="tag">Short</span><strong><span class="todo">[Short title]</span></strong><small>Add once published.</small></a>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap two">
  <div>
    <span class="eyebrow">About the channel</span>
    <h2 style="font-size:clamp(2.2rem,5vw,3.2rem)">Made by The Coefficient Team</h2>
    <p style="color:#dbe1f2">The Coefficient is made by The Coefficient Team, fans of the European game. Built by <a href="https://ali-ozkalay.pages.dev" style="color:#78DCAA">Ali O. Ozkalay</a>. Match data comes from ESPN public feeds. All graphics are original.</p>
    <a class="btn btn-ghost" href="/about.html">More about The Coefficient</a>
  </div>
  <div class="figure"><img src="/assets/img/logo-card-16x9.jpg" alt="The Coefficient title card: Data. Tactics. European Football." width="1280" height="720" loading="lazy"></div>
</div></section>
{subband}
''')

# ---------- VIDEOS ----------
page('videos.html','Videos','Watch The Coefficient: daily Shorts, data-driven match previews, club tier rankings and how-to-read-a-game lessons on European football.',f'''
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Watch</span><h1>Videos</h1>
  <p class="lead" style="margin-left:0">Daily Shorts, match previews, club tier rankings and how-to-read-a-game lessons. Everything lives on YouTube.</p>
  <div class="cta-row" style="justify-content:flex-start">
    <a class="btn btn-sub" href="{SUB}" target="_blank" rel="noopener">{YT}Subscribe</a>
    <a class="btn btn-ghost" href="{HANDLE}" target="_blank" rel="noopener">Open the channel</a>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Auto-updating</span><h2>Latest uploads</h2></div></div>
  <!-- This embed plays the channel's "uploads" playlist, so it updates by itself as new videos are published.
       It will show an empty/unavailable player until the first public upload exists. -->
  <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/videoseries?list={UPLOADS}" title="The Coefficient: latest uploads" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Series</span><h2>Browse by format</h2></div></div>
  <div class="grid g3">
    <a class="video ph" href="{CH}/shorts" target="_blank" rel="noopener" style="background-image:url(/assets/img/banner-1920.jpg)"><span class="tag">Daily</span><strong>Shorts</strong><small>One tactical idea or stat in under a minute.</small></a>
    <a class="video ph" href="{CH}/videos" target="_blank" rel="noopener" style="background-image:url(/assets/img/banner-1920.jpg)"><span class="tag">Weekly</span><strong>Match Previews</strong><small>Data-driven looks at the biggest European games. For learning, not betting.</small></a>
    <a class="video ph" href="{CH}/videos" target="_blank" rel="noopener" style="background-image:url(/assets/img/banner-1920.jpg)"><span class="tag">Rankings</span><strong>Club Tier Rankings</strong><small>Level 1 to 5: squad, organization and structure.</small></a>
    <a class="video ph" href="{CH}/videos" target="_blank" rel="noopener" style="background-image:url(/assets/img/banner-1920.jpg)"><span class="tag">Lessons</span><strong>How to Read a Game</strong><small>For players, parents, coaches and young fans.</small></a>
    <a class="video ph" href="{CH}/playlists" target="_blank" rel="noopener" style="background-image:url(/assets/img/banner-1920.jpg)"><span class="tag">Playlists</span><strong><span class="todo">[Playlist name]</span></strong><small>Link a playlist here once created.</small></a>
    <a class="video ph" href="{CH}/playlists" target="_blank" rel="noopener" style="background-image:url(/assets/img/banner-1920.jpg)"><span class="tag">Playlists</span><strong><span class="todo">[Playlist name]</span></strong><small>Link a playlist here once created.</small></a>
  </div>
</div></section>
{subband}
''')

# ---------- ABOUT ----------
page('about.html','About','About The Coefficient: European football broken down the way a coach and an analyst see it, using public data from FBref, Understat, Transfermarkt and UEFA.',f'''
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">About</span><h1>European football,<br>explained with data</h1>
</div></section>

<section><div class="wrap two">
  <div class="prose">
    <p>The Coefficient breaks down the game the way a coach and an analyst see it: formations, pressing, build-up patterns, xG and the numbers behind every result.</p>
    <p>It's made by The Coefficient Team, fans of the European game. The goal is simple: help players, parents, coaches and young fans learn to see the game differently.</p>
    <p>Built and run by <a href="https://ali-ozkalay.pages.dev">Ali O. Ozkalay</a> with a small team of AI helpers. Educational analysis only — never betting odds.</p>
  </div>
  <div class="figure"><img src="/assets/img/logo-card-16x9.jpg" alt="The Coefficient title card" width="1280" height="720" loading="lazy"></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">The format</span><h2>What we make</h2></div></div>
  {pillars}
</div></section>

<section style="padding-top:0"><div class="wrap prose">
  <h2>Leagues we cover</h2>
  <ul class="pill-list"><li>Champions League</li><li>Premier League</li><li>La Liga</li><li>Serie A</li><li>Bundesliga</li><li>Süper Lig</li></ul>

  <h2>How we work</h2>
  <ul>
    <li><strong>Public data.</strong> Stats come from public sources such as FBref, Understat, Transfermarkt and UEFA, and each video credits its source.</li>
    <li><strong>Original graphics.</strong> All graphics are original. No broadcaster footage or music is used.</li>
    <li><strong>AI disclosure.</strong> Any AI-generated footage used in our videos is disclosed.</li>
    <li><strong>No gambling content.</strong> Previews and probability models are learning tools, not predictions or betting advice.</li>
  </ul>
  <p class="note">Educational analysis only. Nothing on this site or the channel is betting advice.</p>
</div></section>
{subband}
''')

# ---------- CONTACT ----------
page('contact.html','Contact','Contact The Coefficient for business inquiries, collaborations, media requests or questions about a video.',f'''
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Get in touch</span><h1>Contact &amp; business inquiries</h1>
  <p class="lead" style="margin-left:0">Collaborations, sponsorships, media requests or a question about a video. Send a message and we'll get back to you.</p>
</div></section>

<section><div class="wrap two" style="align-items:start">
  <!-- CONTACT FORM
       Works today with no backend: it opens the visitor's email app (mailto).
       To receive submissions without an email app, create a free form at formspree.io (or use Netlify Forms)
       and replace the action below with action="https://formspree.io/f/YOUR_FORM_ID" method="POST" and remove enctype. -->
  <form action="mailto:{EMAIL}" method="post" enctype="text/plain">
    <div><label for="name">Name</label><input id="name" name="name" autocomplete="name" required></div>
    <div><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
    <div><label for="topic">Topic</label>
      <select id="topic" name="topic">
        <option>Business / sponsorship</option><option>Collaboration</option><option>Media / press</option><option>Question about a video</option><option>Other</option>
      </select></div>
    <div><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
    <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div><button class="btn btn-sub" type="submit">Send message</button></div>
  </form>
  <div>
    <div class="card" style="margin-bottom:22px">
      <h3>Email</h3>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="card">
      <h3>YouTube</h3>
      <p><a href="{HANDLE}" target="_blank" rel="noopener">@TheCoefficient-g8c</a></p>
    </div>
  </div>
</div></section>
''')

# ---------- 404 ----------
page('404.html','Page not found','Page not found.',f'''
<section class="hero"><div class="wrap">
  <p class="kicker">Offside</p>
  <h1>404</h1>
  <div class="rule"></div>
  <p class="lead">That page isn't on the team sheet. Head back to the home page or catch the latest Shorts on YouTube.</p>
  <div class="cta-row"><a class="btn btn-ghost" href="/">Back to home</a><a class="btn btn-sub" href="{SUB}" target="_blank" rel="noopener">{YT}Subscribe</a></div>
</div></section>
''')

open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nSitemap: {DOM}/sitemap.xml\n')
open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{DOM}/{"" if f=="index.html" else f}</loc></url>\n' for f,_ in NAV)+'</urlset>\n')
open(os.path.join(OUT,'site.webmanifest'),'w').write('{"name":"The Coefficient","short_name":"Coefficient","icons":[{"src":"/assets/img/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/assets/img/logo-512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#041030","background_color":"#041030","display":"standalone","start_url":"/"}\n')
print('built')
