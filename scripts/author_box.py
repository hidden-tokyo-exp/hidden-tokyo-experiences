#!/usr/bin/env python3
"""Add the guide illustration (hide-avatar.svg) to blog posts and tour pages.

- Blog posts (blog/*.html except index, _scheduled/*.html): author box before </article>,
  and the JSON-LD author gets an image and url.
- Tour pages (tours/*.html): "Your guide" box before the booking box.
Idempotent: pages that already have <!--author-box--> are skipped.
"""
import glob, re, sys

SITE = "https://hidden-tokyo-exp.github.io/hidden-tokyo-experiences/"
BOX = '''<!--author-box-->
<aside style="display:flex;gap:1rem;align-items:center;margin:2.4rem 0 0;padding:1.1rem 1.2rem;background:#fff;border:1px solid #e3d7c4;border-radius:14px;">
<img src="../hide-avatar.svg" alt="Illustration of Hide, your guide" width="72" height="72" style="width:72px;height:72px;border-radius:50%;flex:none;" loading="lazy">
<div style="font-size:.92rem;line-height:1.55;"><strong>{title}</strong><br>{text} <a href="../#story">About Hide &rarr;</a></div>
</aside>
'''
BLOG = dict(title="Written by Hide",
            text="A local guide based in Kiyose, west Tokyo. I walk these routes with small groups and write about what I find on the way.")
TOUR = dict(title="Your guide: Hide",
            text="Born and raised in Tokyo, based in Kiyose. I guide every tour myself, in English, for small groups.")

def add_blog(src):
    if "<!--author-box-->" in src or "</article>" not in src:
        return src
    i = src.rindex("</article>")
    src = src[:i] + BOX.format(**BLOG) + src[i:]
    return src.replace('"author":{"@type":"Person","name":"Hide"}',
        '"author":{"@type":"Person","name":"Hide","url":"%s#story","image":"%shide-avatar.png"}' % (SITE, SITE))

def add_tour(src):
    if "<!--author-box-->" in src or '<div class="cta-box">' not in src:
        return src
    return src.replace('<div class="cta-box">', BOX.format(**TOUR) + '<div class="cta-box">', 1)

def run(paths, fn):
    n = 0
    for p in paths:
        s = open(p, encoding="utf-8").read(); t = fn(s)
        if t != s:
            open(p, "w", encoding="utf-8").write(t); n += 1
    return n

if __name__ == "__main__":
    posts = [p for p in glob.glob("blog/*.html") + glob.glob("_scheduled/*.html") if not p.endswith("index.html")]
    print("blog:", run(posts, add_blog), "tours:", run(glob.glob("tours/*.html"), add_tour))
