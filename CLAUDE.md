# Rules for blog posts (LP, Substack, Medium)

Added 2026-11-01 after the owner's review: posts read like ads, were thin, and thumbnails did not match. These rules apply to every new post in `_scheduled/` and `blog/`, and to the Substack and Medium copies.

Model post: `blog/totoro-forest-day-trip-from-tokyo-without-a-car.html`. Match its structure, length and amount of promotion.

## 0. Pick the topic from the story bank
- Read `content/story-bank.md` first and follow its "How to use" steps: add new note posts, pick the next `ready` theme, mark it used, and warn the owner in the push notification when fewer than 4 themes are `ready`.

## 1. Build the post around real stories from note
- Before writing, read 2-3 of the owner's past note posts on the topic (https://note.com/hide3399). In a Chrome tab on note.com:
  - list: `fetch('/api/v2/creators/hide3399/contents?kind=note&page=N')`
  - body: `fetch('/api/v3/notes/<key>')` → `data.body`
- Retell the real moments in English (a guest's remark, an exchange with a shop owner, a small discovery on the route) and make them the core of the post.
- Never invent experiences. Refer to guests by country only ("a guest from Germany"), no full names.

## 2. Promotion only at the end
- No sales pitch at the top or in the middle. The post must work on its own: how to get there, time, route, closing days, cautions.
- One closing paragraph: "I guide this route in small groups..." with the tour page / GYG link. Do not use the big `cta-box`.

## 3. A different thumbnail every time
- The first photo (thumbnail, `<!--thumb:-->`, og:image, JSON-LD image) must not be used as a thumbnail by any other post in `blog/index.html` or `_scheduled/`.
- Use the owner's own photos that fit the topic. First choice: photos inside the note posts read in step 1. No photos where guests' faces are visible.
- How to add a note photo to this repo: in Chrome, open `github.com/hkidachi3399/hidden-tokyo-experiences/upload/main`, add a `message` listener that puts received Files into `input[type=file]` via DataTransfer and fires `change`, then `window.open('https://note.com/hide3399')`. In the child tab, fetch the image, resize on a canvas to 1200px wide, JPEG 0.82, and `window.opener.postMessage({hteFiles:[file]}, 'https://github.com')`. Commit on GitHub, then `git pull`.
- Name files `<topic>-<subject>.jpg` (e.g. `totoro-hedge.jpg`). Look at every imported photo and check that it matches its caption.
- Put 2-4 photos in the body, each with a short caption.

## 4. Substack and Medium copies
- Paste the LP body HTML (absolute `https://hkidachi3399.github.io/hidden-tokyo-experiences/...` image URLs) into the editor with a synthetic `ClipboardEvent('paste')`; both Substack and Medium re-host the images.
- Substack: before scheduling, check that "Social preview" in the publish panel shows the post's first photo, not the logo or subscribe card.
- Substack, already-scheduled draft: after pasting, the old body may remain below the new signature; delete everything after the first signature line. The publish panel cannot be opened without un-scheduling, so set the thumbnail with `PUT /api/v1/drafts/<id>` `{cover_image: <first image src from draft_body>}` and confirm `postSchedules` is unchanged.

## Do not
- The owner's real name, employer or day job. "licensed" (use "insured" if needed).
