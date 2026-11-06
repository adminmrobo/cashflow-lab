# 10-1번 「현금흐름표 연구실」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | index.html |
| 모드 / 주 앵커 | 교과서 모드 / D 생활: 물탱크 방 (회계 팩 P11), 보조 B 연구실(⑦ 프롬프트) |
| 분야 | 4 회계학(주) + 1 인공지능(보조) |
| 시즌 | 기본 |
| 대결 | AI가 짠 현금흐름표를 검산 없이 제출할까 → 결과 F(초파리 승), 공시와의 차이 0.0억 vs 4.2억 |
| 새로 그릴 그림 | P1 2장 (cover_index, sc_101_hero) · P2 2장 · P3 1장 |
| 재사용 | 캐릭터 표정 21종 (기본 팩 character_pack 1.3) |
| 그림이 없을 때 | 페이지는 기본 팩 표정 그림 + CSS 대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: 캐릭터 팩 18-3, 고정 외형: 캐릭터 팩 18-4 그대로
- 장소: 연구실 안의 물탱크 방 — 큰 유리 탱크, 들어오는 관과 나가는 관, 숫자 없는 수위 눈금
- 장소 영어 묘사: *a water tank room with an inflow pipe and an outflow pipe, water level marks without numbers, purple lab light*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 0 | cover_index | L | 1920×1080 | 새로 (COVER_00_index.md) | P1 | 맨 위 글 표지 | CSS 대체 표지 + 표정 그림 넷 |
| 1 | sc_101_hero | E | 1200×800 | 새로 | P1 | (다음 판) 히어로 무대 | 히어로 대화창 |
| 2 | cut_101_lv4 | G | 960×540 | 새로 | P2 | ④ 사례: 투자 유치 관 | 없음 |
| 3 | cut_101_lv8 | G | 960×540 | 새로 | P2 | ⑧ AI 코드: 조수가 화면의 코드를 읽음 | 없음 |
| 4 | thumb_101 | I | 600×400 | 새로 (cover_index 자르기) | P2 | 목차 카드 | 색 카드 |
| 5 | og_101 | K | 1200×630 | 새로 | P3 | 공유 미리보기 | 없음 |
| — | doc_front·think·judge·magic, asst_smile·firm·report·spark, fly_clip·point·arms·coffee·magnify, robo_smile·coin·sigh·calc 등 21종 | A~D | 96 | 재사용 | — | 말풍선·대결·표지 대체 | — |

## 3. 새로 그릴 그림 상세

### 3-1. `sc_101_hero` — 수위와 물이 어긋난 탱크 앞의 넷
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 구도 | 탱크가 가운데, 초파리 왼쪽(오른쪽을 봄), 주판봇 오른쪽(왼쪽을 봄), 박사 가운데 뒤, 조수 오른쪽 옆 |
| 피할 것 | 승패 암시, 글자, 숫자 |
| 대체 글 | 물탱크의 수위 눈금과 실제 물 높이가 어긋난 것을 네 캐릭터가 바라보는 연구실 장면 |

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a water tank room with an inflow pipe and an outflow pipe, water level marks without numbers, purple lab light, a painted level mark on the glass tank sits higher than the real water surface, chibi scientist with thin teal rectangular glasses and spiky black hair with one white streak in a white lab coat over black vest and tie standing at the back center with a hand on his chin, anthropomorphic fruit fly researcher with big red compound eyes and a blue helmet with a gold stripe on the left facing right holding a magnifying glass, boxy beige retro CRT-monitor robot with a dark green screen face and a short antenna topped with a red-brown abacus bead on tank treads on the right facing left holding a wooden abacus, girl researcher with long pink hair in two round buns and a navy streak in a white lab coat over lavender hoodie and jeans at the side holding a clipboard with blank striped lines, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-2. `cut_101_lv4` — 두 갈래 관: 빠지는 물과 들어오는 물
| 항목 | 내용 |
|---|---|
| 판 · 크기 | G · 960×540 |
| 구도 | 왼쪽 관에서 물이 빠지고 오른쪽 큰 관으로 물이 쏟아져 들어온다. 초파리가 왼쪽 관을, 주판봇이 오른쪽 관을 본다 |
| 대체 글 | 영업에서 빠지는 물과 투자 유치로 들어오는 물을 두 캐릭터가 각각 살피는 컷 |

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, 16:9 illustration panel, a glass water tank with a thin left pipe draining water with a reddish glow and a thick right pipe pouring water in with a greenish glow, anthropomorphic fruit fly researcher with big red compound eyes and a blue helmet on the left facing right inspecting the draining pipe with a magnifying glass, boxy beige retro CRT-monitor robot with a dark green screen face and an abacus bead antenna on the right facing left looking up at the strong inflow, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-3. `cut_101_lv8` — 화면의 코드를 읽는 조수
| 항목 | 내용 |
|---|---|
| 판 · 크기 | G · 960×540 |
| 구도 | 조수가 모니터 앞에서 줄무늬(글자 없음) 코드 화면을 가리키고, 초파리가 어깨 너머로 본다 |
| 대체 글 | 조수와 초파리 연구원이 모니터에 뜬 코드 줄을 함께 읽는 컷 |

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 16:9 illustration panel, girl researcher with long pink hair in two round buns and a navy streak, white lab coat over lavender hoodie, jeans, pointing at a monitor showing rows of colored blank code lines without letters, anthropomorphic fruit fly researcher with big red compound eyes and a blue helmet with a gold stripe looking over her shoulder, a small green check mark glowing at the corner of the screen, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 4. 일관성 지침
- 참고 이미지: 기본 팩 설정샷 k01~k12와 표정 그림
- 같은 캐릭터는 같은 세션에서, 시드 고정 가능하면 고정
- 표정만 바꿀 때: *same character, same size and position, only change the facial expression and pose to ...*

## 5. 매니페스트
```json
{
  "page": "10-1_cashflow",
  "anchor": "D:water-tank-room",
  "season": "default",
  "duel": {"result": "F", "gap": 4.2},
  "images": [
    {"key":"cover_index","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover","fallback":"css-pixel-four","alt":"밤의 연구실 물탱크 방에서 네 캐릭터가 세 갈래 관으로 드나드는 물과 어긋난 수위 눈금을 살피는 표지"},
    {"key":"sc_101_hero","plate":"E","size":[1200,800],"status":"new","priority":"P1","slot":"hero-stage","fallback":"hero-dialog","alt":"물탱크의 수위 눈금과 실제 물 높이가 어긋난 것을 네 캐릭터가 바라보는 연구실 장면"},
    {"key":"cut_101_lv4","plate":"G","size":[960,540],"status":"new","priority":"P2","slot":"lv4","fallback":"none","alt":"영업에서 빠지는 물과 투자 유치로 들어오는 물을 두 캐릭터가 각각 살피는 컷"},
    {"key":"cut_101_lv8","plate":"G","size":[960,540],"status":"new","priority":"P2","slot":"lv8","fallback":"none","alt":"조수와 초파리 연구원이 모니터에 뜬 코드 줄을 함께 읽는 컷"},
    {"key":"thumb_101","plate":"I","size":[600,400],"status":"new","priority":"P2","slot":"index-card","fallback":"color-card","alt":""},
    {"key":"og_101","plate":"K","size":[1200,630],"status":"new","priority":"P3","slot":"og","fallback":"none","alt":""}
  ]
}
```
