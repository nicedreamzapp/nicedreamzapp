<div align="center">

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/hero.svg" width="100%" alt="Matt Macosko. Something was eating my chickens. That is the whole origin story. Local AI on Apple Silicon, Humboldt County, CA, open to work.">

[![GitHub followers](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-followers-nicedreamzapp-c923c7.svg)](https://github.com/nicedreamzapp)
[![Mentioned in Awesome Claude Code](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-mentioned-in-awesome-claude-code-fc60a8-500728.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![Stars](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-claude-code-local-af34a8.svg)](https://github.com/nicedreamzapp/claude-code-local)
[![App downloads](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/app-downloads-2c2e02.svg)](#app-stats)
[![New this week](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/app-week-20cec2.svg)](#app-stats)

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/coop.gif?v=2" width="760" alt="A local vision model tagging every chicken in the yard, running offline on an Apple Silicon Mac">

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/stats.svg" width="100%" alt="5 of 5 apps approved on both stores. 23/23 parity tests. 601 objects named offline. 13 always-on agents across 3 machines.">

</div>

<br>

<a id="story"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s01-story.svg" width="100%" alt="01. The story so far: from a chicken coop to robots that help people">

### 🐔 Something was eating my chickens.

That is the whole origin story.

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/story-1.svg" width="100%" alt="Chickens, a camera that sees at night, a vision model small enough for a robot">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/story-2.svg" width="100%" alt="AI on my own hardware, RealTime AI Cam, a robot that grows food">

| | One step at a time |
|:---:|---|
| 🌙 | Protecting them needed $\color{#0284c7}{\textsf{\textbf{a camera that could see at night}}}$. |
| 🤖 | That needed $\color{#7c3aed}{\textsf{\textbf{a vision model small enough to live on a robot}}}$. |
| 💻 | That needed $\color{#2563eb}{\textsf{\textbf{AI running on my own hardware}}}$ instead of somebody else's cloud. |
| 📷 | That became **[RealTime AI Cam](https://github.com/nicedreamzapp/RealTimeAICam)**: it names **601** objects, $\color{#16a34a}{\textsf{\textbf{fully offline}}}$. |
| 🦯 | Along the way it turned out to $\color{#e11d48}{\textsf{\textbf{help blind people see}}}$, with no internet. |
| 🌱 | Next: [a robot that grows food](#long-arc). |
| 🦿 | The bigger idea: $\color{#d97706}{\textsf{\textbf{robots that give people back what they have lost}}}$. |

🧪 Dozens of repos later I am somehow $\color{#7c3aed}{\textsf{\textbf{doing neuroscience}}}$, and every one of them still traces back to the coop.

### 👁️ The model that does the describing

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/narrator-tiles.svg" width="100%" alt="2B version 99.0% on 400 held-out photos. 0.8B at 622 MB, 98.5%. About a dozen versions over one month. 27B teacher.">

| | |
|:---:|---|
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-model.svg" alt="My model"> | **Vision Narrator 0.8B** is RealTime AI Cam's describer, and it's my own model: [on Hugging Face](https://huggingface.co/divinetribe/Vision-Narrator-0.8B-4bit-mlx). A LoRA fine-tune of Qwen3.5-0.8B, taught by a **27B** teacher. |
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-data.svg" alt="Data"> | Trained on $\color{#0284c7}{\textsf{\textbf{VizWiz}}}$: photos taken by blind people (CC BY 4.0). About **a dozen versions** over **one month**. |
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-podcast.svg" alt="Podcast"> | I'm a guest on the $\color{#e11d48}{\textsf{\textbf{Blind Android Users podcast}}}$, **Saturday, Oct 24, 2026**. |

<br>

<a id="open-to-work"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s02-open-to-work.svg" width="100%" alt="02. Open to work: local AI and Apple Silicon inference">

**📬 [matt@ineedhemp.com](mailto:matt@ineedhemp.com)** · looking for a role building on-device / local AI.

📚 Case studies of nine of these projects, with the bugs and the measured numbers: **[nicedreamzwholesale.com/software/case-studies](https://nicedreamzwholesale.com/software/case-studies/)**

| | Highlight |
|:---:|---|
| 🧠 | **[claude-code-local](https://github.com/nicedreamzapp/claude-code-local)**: Claude Code running 100% on-device on Apple Silicon, with its own MLX server and tool-call parser. **<!--CCL:START-->3,300+ stars, 637 forks<!--CCL:END-->**, featured in [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code), and fixes merged from contributors on hardware I don't own. |
| 🍎 | **Upstream in Apple's MLX**: [Muse Glimmer (Meta) text model support](https://github.com/ml-explore/mlx-lm/pull/1710) merged into `ml-explore/mlx-lm` (+302 lines). Thanks to [@zcbenz](https://github.com/zcbenz) for the review and merge. |
| 👁️ | **[nemotron-omni-mlx](https://github.com/nicedreamzapp/nemotron-omni-mlx)**: first open Apple Silicon runtime for NVIDIA Nemotron Omni's vision and audio towers, **23/23 parity tests** against NVIDIA's PyTorch reference. |
| 🏁 | **[Agent-12](https://github.com/nicedreamzapp/agent12)**: a filesystem-judged local agent leaderboard, independently reproduced by [@galashko](https://github.com/galashko). |
| 🏪 | **[HQ: the AI system that runs my shop](https://github.com/nicedreamzapp/how-my-shop-runs)**: orders from checkout to the door, four-second shipping labels, support drafts I approve, and agents on four machines sharing one memory. |
| 📱 | **Shipped apps**: <!--APPS-LINE:START-->5 apps on the App Store and Google Play, **2,233 downloads** so far (1,502 App Store, 731 Google Play), 43 new on iPhone in the last week.<!--APPS-LINE:END--> |

<br>

<a id="apps"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s03-apps.svg" width="100%" alt="03. Apps: iPhone and Android">

Every app, both stores. Private by default, pay once (or nothing), no subscriptions.

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-blue.svg" width="100%" height="6" alt="">
<h3>🎵 Song Forge</h3>
Describe a song, get a finished original. Any genre, 19 languages, rendered on my Macs at home, never stored. 10 free songs, no account, no email.
<br><br>
<a href="#app-stats"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/app-song-forge-1c07bd.svg" alt="downloads"></a><br>
<a href="https://apps.apple.com/us/app/id6788616929"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-app-store-0d96f6-2bf332.svg" alt="App Store"></a>
<a href="https://play.google.com/store/apps/details?id=com.nicedreamz.ownatune"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-google-play-01875f-9cd304.svg" alt="Google Play"></a>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-blue.svg" width="100%" height="6" alt="">
<h3>📷 RealTime AI Cam</h3>
Point your camera, it names 601 objects. Fully offline.
<br><br>
<a href="#app-stats"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/app-realtime-ai-cam-329e88.svg" alt="downloads"></a><br>
<a href="https://apps.apple.com/us/app/id6751230739"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-app-store-0d96f6-2bf332.svg" alt="App Store"></a>
<a href="https://play.google.com/store/apps/details?id=com.mattmacosko.realtimeaicam"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-google-play-01875f-9cd304.svg" alt="Google Play"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-blue.svg" width="100%" height="6" alt="">
<h3>🚀 RealTime Space</h3>
Fly a real-physics starship through the solar system and 8,920 real stars.
<br><br>
<a href="#app-stats"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/app-realtime-space-d1c822.svg" alt="downloads"></a><br>
<a href="https://apps.apple.com/us/app/id6788646103"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-app-store-0d96f6-2bf332.svg" alt="App Store"></a>
<a href="https://play.google.com/store/apps/details?id=com.nicedreamz.realtimespace"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-google-play-01875f-9cd304.svg" alt="Google Play"></a>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-blue.svg" width="100%" height="6" alt="">
<h3>🌳 Brainforest</h3>
2,000+ K-4 lessons, reads everything aloud, fully offline, one-time $1.99. No ads, no tracking. Built for my daughter.
<br><br>
<a href="#app-stats"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/app-brainforest-dc7d28.svg" alt="downloads"></a><br>
<a href="https://apps.apple.com/us/app/id6788301765"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-app-store-0d96f6-2bf332.svg" alt="App Store"></a>
<a href="https://play.google.com/store/apps/details?id=com.brainforest.app"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-google-play-01875f-9cd304.svg" alt="Google Play"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-blue.svg" width="100%" height="6" alt="">
<h3>🐝 Hive Strike</h3>
One bee against sixteen worlds, sixteen bosses and seventy-five kinds of bug. Every sprite, background, animated scene and music bed generated locally on one Mac, no cloud, no stock art.
<br><br>
<a href="#app-stats"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/app-hive-strike-6b634f.svg" alt="downloads"></a><br>
<a href="https://apps.apple.com/us/app/id6808332314"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-app-store-0d96f6-2bf332.svg" alt="App Store"></a>
<a href="https://play.google.com/store/apps/details?id=com.nicedreamz.hivestrike"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-google-play-01875f-9cd304.svg" alt="Google Play"></a>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-blue.svg" width="100%" height="6" alt="">
<h3>🤖 Open source</h3>
Android source ships in each repo's <code>android/</code> folder.
<br><br>
✅ <b>Review record: every app approved on both stores.</b> Five of five on the App Store and five of five on Google Play.
</td>
</tr>
</table>

<br>

<a id="app-stats"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s04-app-stats.svg" width="100%" alt="04. App stats: updated automatically">

<!--APP-STATS:START-->
> _Updated automatically **Oct 21, 2026** from Apple's sales reports and Google Play's install reports. Downloads are first-time App Store downloads (no updates or re-downloads) plus Google Play installs; Google runs about two weeks behind._

| App | Live since | Downloads | App Store | Google Play | New on iPhone, last 7 days | App Store rating |
|---|---|---:|---:|---:|---:|:---:|
| **RealTime AI Cam** | Aug 2025 | **1,672** | 1,165 | 507 | 14 | ★ 5.0 (2) |
| **Song Forge** | Jul 2026 | **278** | 111 | 167 | 5 | – |
| **RealTime Space** | Jul 2026 | **209** | 163 | 46 | 21 | – |
| **Brainforest** | Jul 2026 | **68** | 61 | 7 | 2 | ★ 5.0 (1) |
| **Hive Strike** | Sep 2026 | **6** | 2 | 4 | 1 | – |
| **Total** | | **2,233** | **1,502** | **731** | **43** | |

**New iPhone downloads per week, last 8 weeks:** 48 → 40 → 85 → 115 → 72 → 148 → 85 → 43 (-42 vs the week before).
<!--APP-STATS:END-->

<br>

<a id="just-shipped"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s05-just-shipped.svg" width="100%" alt="05. Just shipped">

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-pink.svg" width="100%" height="6" alt="">
<h3>🖥️ <a href="https://github.com/nicedreamzapp/trinidad-head">Trinidad Head</a></h3>
My own terminal, built from scratch for Windows and Mac.<br><br>
✨ Glass windows with a neon glow<br>
🎨 A different color for every open window<br>
🔎 Your own questions easy to spot when you scroll back through an AI chat
<br><br>
<a href="https://nicedreamzwholesale.com/software/trinidad-head/">Project page →</a>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-pink.svg" width="100%" height="6" alt="">
<h3>👁️ <a href="https://github.com/nicedreamzapp/nemotron-omni-mlx">nemotron-omni-mlx</a></h3>
NVIDIA's <a href="https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16">Nemotron Omni</a> sees, hears, and reasons.<br>
Its vision and audio towers had no open runtime for Apple Silicon. So I wrote one.<br><br>
✅ Pure MLX, MIT<br>
✅ <b>23/23 parity tests</b> against NVIDIA's PyTorch reference<br>
⚡ <b>67.7 tok/s</b> with an image, end to end<br>
⚡ <b>110.5 tok/s</b> with audio, end to end<br>
💻 On an M5 Max, wifi off
<br><br>
<sub>Credit to NVIDIA for the open weights and <a href="https://huggingface.co/mlx-community/NVIDIA-Nemotron-3-Nano-Omni-30B-A3B-4bit">yayr</a> for the 4-bit conversion.</sub>
</td>
</tr>
</table>

<br>

<a id="building"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s06-building.svg" width="100%" alt="06. What I'm actually building">

### 🧩 Most of these repos look standalone. They're not.

They're $\color{#7c3aed}{\textsf{\textbf{one system}}}$ spread across **three machines** that talk to each other **24/7**.

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/building-tiles.svg" width="100%" alt="3 machines, 24/7, 13 always-on agents, $0 per call">

| | Machine | Job |
|:---:|---|---|
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-workstation.svg" alt="Workstation"> | **M5 Max MacBook Pro · 128 GB** | $\color{#7c3aed}{\textsf{\textbf{Heavy compute}}}$: model inference, video, image, training |
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-workhorse.svg" alt="Workhorse"> | **M4 Mac mini · 64 GB** | $\color{#0284c7}{\textsf{\textbf{Always-on workhorse}}}$: autonomous agents, FiaOS web shell, free Claude for the whole mesh |
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-gateway.svg" alt="Gateway"> | **Hostinger VPS** | $\color{#d97706}{\textsf{\textbf{Public gateway}}}$: HQ Dashboard, the Ohm chat agent, sites, cron |

### 💡 The idea

- ⚡ Apple Silicon is fast enough now that the everyday AI I want $\color{#16a34a}{\textsf{\textbf{does not need a cloud subscription}}}$.
- 🏠 $\color{#0284c7}{\textsf{\textbf{Build local-first}}}$, stay useful when the internet goes down.
- 🔒 The same stack is $\color{#7c3aed}{\textsf{\textbf{airgap-ready}}}$, which matters to the law / medical / compliance-sensitive firms I work with through Nice Dreamz LLC.

### 🤖 **13** always-on agents run across those nodes

| | Agent |
|:---:|---|
| 🐙 | A $\color{#7c3aed}{\textsf{\textbf{GitHub watcher}}}$ that drafts issue replies with local AI and texts me the draft |
| ☀️ | A **9am** $\color{#d97706}{\textsf{\textbf{iMessage business briefing}}}$ |
| 📬 | $\color{#0284c7}{\textsf{\textbf{Email triage}}}$ |
| 👀 | A $\color{#e11d48}{\textsf{\textbf{Reddit brand watcher}}}$ |
| 🔑 | The trick that powers it all: `mini_claude`, which lets every agent use my Claude Max plan for $\color{#16a34a}{\textsf{\textbf{zero dollars per call}}}$ |

<details>
<summary><i>the wiring diagram, if you like that sort of thing</i></summary>

```
                          ┌─────────────────────────────┐
                          │   iPhone (iMessage bridge)  │
                          │   ask · send · image · vid  │
                          └────────────┬────────────────┘
                                       │
       ┌───────────────────────────────┼───────────────────────────────┐
       │                               │                               │
┌──────▼──────────┐         ┌──────────▼──────────────┐     ┌──────────▼────────┐
│  M5 Max         │         │   Mac mini (always-on)  │     │  VPS (Hostinger)  │
│  workstation    │◀──SSH──▶│   the workhorse         │◀───▶│   gateway         │
└─────────────────┘         └─────────────────────────┘     └───────────────────┘
```

</details>

<br>

<a id="airgap"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s07-airgap.svg" width="100%" alt="07. AirGap: a skill, not a product">

🔒 **AirGap is my name for the full private-AI build.**

- 🖥️ A complete AI workstation on **one** Mac
- 📴 Wifi off, nothing leaving the building
- 🧰 It started as a packaged offering; these days I treat it as a capability I keep sharp rather than something I sell
- 🔓 Everything it needs is open source on this page, so any competent IT person can stand one up without me. That's the point.
- 📬 If your firm handles data that can't touch the cloud and you want one built and your team trained on it, email [info@nicedreamzwholesale.com](mailto:info@nicedreamzwholesale.com)

[What it looks like →](https://nicedreamzwholesale.com/airgap/) · [Why it matters now →](https://nicedreamzwholesale.com/2026/05/22/the-heppner-ruling-warner-v-gilbarco-and-what-confidential-ai-actually-has-to-mean/)

<br>

<a id="front-five"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s08-front-five.svg" width="100%" alt="08. The front five, sorted by GitHub stars">

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-amber.svg" width="100%" height="6" alt="">
<h3><a href="https://github.com/nicedreamzapp/claude-code-local">Claude Code Local</a></h3>
<a href="https://github.com/nicedreamzapp/claude-code-local/stargazers"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-claude-code-local-357b31.svg" alt="Stars"></a>
<a href="https://github.com/nicedreamzapp/claude-code-local/network/members"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-forks-claude-code-local-5184c0.svg" alt="Forks"></a>
<br><br>
Run Claude Code 100% on-device on Apple Silicon. Current lineup led by Qwen 3.8 27B and Gemma 4 31B, four modes (code, browser, voice, phone), Anthropic-compatible MLX server, <code>setup.sh</code> picks the right model for your RAM. Your code never leaves your Mac. Featured in <a href="https://github.com/hesreallyhim/awesome-claude-code">Awesome Claude Code</a>.
<br><br>
<code>MLX</code> <code>Apple Silicon</code> <code>Claude Code</code> <code>Python</code>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-amber.svg" width="100%" height="6" alt="">
<h3><a href="https://github.com/nicedreamzapp/NarrateClaude">NarrateClaude + Ohm</a></h3>
<a href="https://github.com/nicedreamzapp/NarrateClaude/stargazers"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-narrateclaude-7426bb.svg" alt="Stars"></a>
<br><br>
Talk to your Mac, hear it reply in your own cloned voice. 100% private, works on a plane, and the Ohm web chat brings the same loop to any browser at zero API cost.
<br><br>
<code>Pocket TTS</code> <code>Apple Silicon</code> <code>Flask</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-amber.svg" width="100%" height="6" alt="">
<h3><a href="https://github.com/nicedreamzapp/browser-agent">Browser Agent</a></h3>
<a href="https://github.com/nicedreamzapp/browser-agent/stargazers"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-browser-agent-f805b6.svg" alt="Stars"></a>
<br><br>
Local MLX models driving Chrome via DevTools Protocol. Handles what other agents can't: cross-origin iframes, Shadow DOM, ProseMirror.
<br><br>
▶ <a href="https://youtu.be/SIuMNa2k6Wc">56-second demo →</a>
<br><br>
<code>MLX</code> <code>Chrome DevTools Protocol</code> <code>Local AI</code>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-amber.svg" width="100%" height="6" alt="">
<h3><a href="https://github.com/nicedreamzapp/browser-broker">Browser Broker</a></h3>
<a href="https://github.com/nicedreamzapp/browser-broker/stargazers"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-browser-broker-b96186.svg" alt="Stars"></a>
<br><br>
One logged-in browser, many agents, nobody fights. Leases each agent an ordinary background tab in your real browser, with your real logins, and every agent sees only its own. ~300 lines, one dependency. Verified on Linux by a stranger who then found a bug in my own docs.
<br><br>
<code>Chrome DevTools Protocol</code> <code>Multi-agent</code> <code>Local AI</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-amber.svg" width="100%" height="6" alt="">
<h3><a href="https://github.com/nicedreamzapp/RealTimeAICam">RealTimeAICam</a></h3>
<a href="https://github.com/nicedreamzapp/RealTimeAICam/stargazers"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-realtimeaicam-b2f1d2.svg" alt="Stars"></a>
<br><br>
The biggest free open-vocabulary detector that fits on an iPhone: 601 classes, OCR, LiDAR depth, all on-device. The seed of the robot's vision stack.
<br><br>
▶ <b><a href="https://www.youtube.com/watch?v=2BEYv-fv-gE">Watch it see the world, fully offline (90 sec)</a></b>
<br><br>
<code>YOLOv8</code> <code>CoreML</code> <code>Swift</code> <code>LiDAR</code>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-amber.svg" width="100%" height="6" alt="">
<h3><a href="https://github.com/nicedreamzapp/claude-screen-to-phone">Claude → Phone</a></h3>
<a href="https://github.com/nicedreamzapp/claude-screen-to-phone/stargazers"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-claude-screen-to-phone-2c6c89.svg" alt="Stars"></a>
<br><br>
Control Claude Code from your iPhone via iMessage. Commands by text; screenshots, recordings, and YES / NO / YES_TO_ALL approval buttons come back.
<br><br>
<code>iMessage</code> <code>AppleScript</code> <code>macOS Automation</code>
</td>
</tr>
</table>

<br>

<a id="daily-drivers"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s09-daily-drivers.svg" width="100%" alt="09. The daily drivers">

| | Repo | One line |
|---|---|---|
| 🌐 | **[FiaOS](https://github.com/nicedreamzapp/FiaOS)** | The Mac mini in a browser tab: live desktop, real PTY shell, voice. The bridge that gives the whole mesh free Claude. |
| 🎥 | **[studio-record](https://github.com/nicedreamzapp/studio-record)** | Screen + facecam recorder with a local HTTP API, so Claude can record itself working. |
| 🛟 | **[claude-failover](https://github.com/nicedreamzapp/claude-failover)** | One command and your `claude -p` agents keep running on a local MLX model when the cloud is down. |
| 🎬 | **[story-forge](https://github.com/nicedreamzapp/story-forge)** | A whole film studio on one laptop. A director keeps going until every shot passes a local vision judge, then cuts, scores and voices the film. Two finished films, no cloud. |

<br>

<a id="long-arc"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s10-long-arc.svg" width="100%" alt="10. The long-arc bet: a robot that grows food">

### 🌱 Here's where all of this is headed.

You hand a robot $\color{#16a34a}{\textsf{\textbf{a bag of seeds}}}$, show it $\color{#0284c7}{\textsf{\textbf{where the hose is}}}$, and a few months later there are $\color{#d97706}{\textsf{\textbf{vegetables on the table}}}$.

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/seeds-strip.svg" width="100%" alt="You hand a robot a bag of seeds, show it where the hose is, and a few months later there are vegetables on the table.">

It $\color{#16a34a}{\textsf{\textbf{plants}}}$, $\color{#0284c7}{\textsf{\textbf{waters}}}$, $\color{#7c3aed}{\textsf{\textbf{weeds}}}$, $\color{#d97706}{\textsf{\textbf{harvests}}}$, $\color{#e11d48}{\textsf{\textbf{carries the food in}}}$, and someday maybe cooks it too.\
☀️ It $\color{#d97706}{\textsf{\textbf{charges from the sun}}}$ and its $\color{#7c3aed}{\textsf{\textbf{whole brain lives inside it}}}$, so it keeps working where there's $\color{#0284c7}{\textsf{\textbf{no internet at all}}}$.

### 🏘️ Now picture dropping two of them in a village

...where $\color{#e11d48}{\textsf{\textbf{people are hungry}}}$ and there's $\color{#0284c7}{\textsf{\textbf{no signal for a hundred miles}}}$.

| | |
|:---:|---|
| 💧 | They $\color{#0284c7}{\textsf{\textbf{dig the well}}}$, |
| 🌾 | $\color{#16a34a}{\textsf{\textbf{plant the rows}}}$, |
| 🧺 | and $\color{#d97706}{\textsf{\textbf{bring in the harvest}}}$. |

That's the science fiction story I'm building toward, and I think we're $\color{#7c3aed}{\textsf{\textbf{closer to it than most people realize}}}$.

### 🧩 Every repo on this page is a piece of it.

| | Piece | What it does |
|:---:|---|---|
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-eyes.svg" alt="Eyes"> | **[RealTime AI Cam](https://github.com/nicedreamzapp/RealTimeAICam)** is the eyes | A vision model that runs fully offline on a phone, and along the way it turned out to help blind people see. |
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-brain.svg" alt="Brain"> | **[Claude Code Local](https://github.com/nicedreamzapp/claude-code-local)** is the brain | The brain without a cloud. |
| <img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/chip-body.svg" alt="Body"> | **The Cemani robot** is the first body | See below. |

📴 Right now I'm scraping the edges, but every piece $\color{#16a34a}{\textsf{\textbf{works with the wifi off}}}$, and that's on purpose.

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-lime.svg" width="100%" height="6" alt="">
<h3>🐓 <a href="https://github.com/nicedreamzapp/CemaniHomesteadRobot">Cemani Homestead Robot</a></h3>
<a href="https://github.com/nicedreamzapp/CemaniHomesteadRobot/stargazers"><img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/github-stars-cemanihomesteadrobot-d8038a.svg" alt="Stars"></a>
<br><br>
Started with protecting my chickens from predators. Now:<br><br>
🚜 A <b>1 kW</b> autonomous tank robot you text from your phone<br>
👁️ <b>601</b>-class vision on a Jetson<br>
📷 Dual PTZ cameras, 3D LIDAR<br>
🪵 It pulls a cart of firewood. Actually.
<br><br>
The honest goal: a Lego-clip-in modular robotics kit running the same local-AI brain as the desk. <a href="https://github.com/nicedreamzapp/VisionBuilder">VisionBuilder</a> trains its eyes from photos on my phone.
<br><br>
<code>Jetson Orin Nano</code> <code>YOLOv8</code> <code>Teensy</code> <code>RPLidar</code> <code>Robotics</code>
</td>
<td width="50%" valign="middle" align="center">
<a href="https://youtu.be/NWnGvvdvRik"><img src="https://img.youtube.com/vi/NWnGvvdvRik/maxresdefault.jpg" width="100%" alt="▶ Watch the 53-second demo"></a>
<br>
<sub>▶ Watch the 53-second demo</sub>
</td>
</tr>
</table>

🦿 **Also on the bench: Run + Sit Exo**, a powered knee exoskeleton design I'm working on. It's a design and prototype, not a finished product.

<br>

<a id="family"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s11-family.svg" width="100%" alt="11. The family project: Brainforest">

### 🌳 [Brainforest](https://nicedreamzwholesale.com/software/brainforest/): built for my daughter, live on both stores

- 📖 2,000+ K-4 lessons with a friendly narrator that reads everything aloud.
- 🦄 Themes she picks (unicorns, dinosaurs, space, cats, Bluey).
- 📈 Difficulty that climbs as she masters skills and gently drops when she struggles.
- 🖱️ Click-only kid-safe interface.
- 🔌 Fully offline, one-time $1.99, no ads, no tracking, no internet needed.
- 🔓 Source is open: [brainforest-app](https://github.com/nicedreamzapp/brainforest-app), iOS and Android in one repo.

`iOS` `Fully Offline` `Adaptive Learning` `Kid-Safe`

<br>

<a id="receipts"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s12-receipts.svg" width="100%" alt="12. Receipts: does local actually work?">

Four real jobs, run one at a time and then in four browser tabs at once, each answer checked by script, no AI judge (Sep 16, 2026, M5 Max, [browser-agent](https://github.com/nicedreamzapp/browser-agent) + [browser-broker](https://github.com/nicedreamzapp/browser-broker)):

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/receipts.svg" width="100%" alt="All four tabs at once: Gemma 4 31B finished in 110 seconds, Qwen 3.8 27B in 176 seconds, both 8 of 8 right">

| Local model | Right answers (4 one at a time + 4 at once) | All four tabs at once |
|---|---:|---:|
| 🟢 Gemma 4 31B (MLX, bf16) | **8/8** | **110 s** |
| 🟣 Qwen 3.8 27B (MLX, bf16) | 8/8 | 176 s |

Every model we run is also scored on real agent tasks at the open [Agent-12 leaderboard](https://nicedreamzapp.github.io/agent12/).

<br>

<a id="stores"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s13-stores.svg" width="100%" alt="13. The stores">

- 🛒 [Divine Tribe](https://ineedhemp.com): vaporizer hardware, American-owned since **2013**
- 🏬 Plus [three more stores](https://marijuanaunion.com)
- 📦 **140+** products, **5,000+** units shipped
- ⚙️ All automated by the mesh above
- 💵 Divine Tribe pays the bills; everything else is downstream

<br>

<details>
<summary><b>🗂️ LAB NOTEBOOK: everything else</b> <i>(click to open: experiments, one-offs, internal builds)</i></summary>

<br>

| Project | What it is |
|---|---|
| [song-forge](https://github.com/nicedreamzapp/song-forge) | The local AI music engine behind the Song Forge app: ACE-Step + Gemma + seed-vc, fully on-device |
| [Parkinson's Vulnerability Predictor](https://github.com/nicedreamzapp/parkinsons-vulnerability-predictor) | ML on 65,000+ cells, 20-gene signature · [1-min video](https://youtu.be/bC4hgeHS9cg) |
| [Family Planner](https://github.com/nicedreamzapp/Family-Planner) | Skylight-style family dashboard on old tablets: voice, OCR, AI assistant |
| [SpeakAnywhere](https://github.com/nicedreamzapp/SpeakAnywhere) | Whisper-powered voice control for the desktop |
| [RealTime Space](https://github.com/nicedreamzapp/RealTime-Space) | The photoreal solar system engine behind the RealTime Space app, iOS and Android in one repo |
| [The Farmstand 3D](https://github.com/nicedreamzapp/the-farmstand-3d) | WebXR marketplace, [live](https://marijuanaunion.com/marketplace) |
| [MattPaint](https://github.com/nicedreamzapp/MattPaint) | Pixel-perfect MS Paint clone, zero dependencies |
| [Heat-N-Clean Glass Oven](https://github.com/nicedreamzapp/Heat-N-Clean-Glass-Oven) | Custom temperature-controlled cleaning kiln, CAD included |
| [job-search-agent](https://github.com/nicedreamzapp/job-search-agent) | Daily AI job scoring against your own background, straight from public Ashby, Greenhouse and Lever boards |
| [dan-aquatic-ecology](https://github.com/nicedreamzapp/dan-aquatic-ecology) | A friend's HSU thesis site, built end-to-end in one sitting |
| [DisclosureDay](https://github.com/nicedreamzapp/DisclosureDay) | SEO + chatbot site for the UFO film |
| [BitcoinPredictor](https://github.com/nicedreamzapp/BitcoinPredictor) | Real-time BTC dashboard with ML signals (trading systems retired 2026) |

**Internal builds (no public repo):** HQ Dashboard (central command: orders, email, shipping, agents), Ohm (the LLM chat agent that bridges the mesh), and an AI customer chatbot trained on the full Divine Tribe lineup.

</details>

<details>
<summary><b>🧰 TECH STACK</b> <i>(click: the usual badge wall)</i></summary>

<br>

<div align="center">

![Python](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-python-3776ab-46035b.svg)
![Swift](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-swift-f05138-ae2b39.svg)
![JavaScript](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-javascript-f7df1e-088fee.svg)
![Apple Silicon](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-apple-silicon-000000-d5b7f3.svg)
![MLX](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-mlx-8b5cf6-c88f0d.svg)
![Claude](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-claude-d97757-7966d2.svg)
![CoreML](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-coreml-2563eb-522705.svg)
![Flask](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-flask-000000-cac63f.svg)
![nginx](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-nginx-009639-21c450.svg)
![Jetson](https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/badges/badge-jetson-orin-76b900-928933.svg)

`Gemma` `Llama` `Qwen` `YOLOv8` `SAM 2.1` `Whisper` `Piper TTS` `WooCommerce` `EasyPost` `Cloudflare Tunnel` `Teensy` `ESP32` `RPLidar`

</div>

</details>

<br>

<a id="why"></a>
<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/s14-why.svg" width="100%" alt="14. Why this exists">

- 🌲 I run [Divine Tribe](https://ineedhemp.com): vaporizer hardware, since **2013**.
- 🏪 [HQ](https://github.com/nicedreamzapp/how-my-shop-runs), the AI system I built, runs the shop side.
- 💵 Everything else is downstream of paying the bills.
- 🏢 **Nice Dreamz LLC** is the umbrella on top.
- 🔒 [AirGap AI](https://nicedreamzwholesale.com/airgap) is the showcase: what a full private-AI build looks like for the kind of firm that can't put its data into a cloud chatbot.
- 🧰 It's a capability I maintain, not a product I'm pushing.
- 🖧 The **three-node** mesh is the demo: it's been my daily driver for **a year and a half**.
- 🛡️ I'm also building the [Cannabis Device Safety Institute](https://cdsi.click) in parallel, a standards body for cannabis-consumption hardware.
- 🤖 The long arc is the robot. Same eyes, different bodies.

**Still figuring it out. No investors. One MacBook, one Mac mini, one VPS, and a lot of late nights.**

<br>

<div align="center">

<img src="https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/assets/profile/bar-pink.svg" width="60%" height="6" alt="">

**[ineedhemp.com](https://ineedhemp.com) · [GitHub](https://github.com/nicedreamzapp) · [LinkedIn](https://www.linkedin.com/in/matt-macosko-34708235/)**

<sub>Built with code, caffeine, and Claude · Humboldt County, CA · the chickens are fine</sub>

</div>
