# 표지 지시문 — 10-1 현금흐름표 연구실

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_index · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | D 생활 — 연구실 안의 물탱크 방 (회계 팩 P11) |
| 주제 은유 | 큰 물탱크 하나에 관 세 개가 연결: 왼쪽 관은 물이 빠져나가고(영업), 가운데 관은 조금 빠지고(투자), 오른쪽 관으로 많은 물이 들어온다(재무). 탱크의 수위 눈금(숫자 없음)과 실제 물 높이가 어긋나 있다 — 장부의 이익과 실제 현금의 차이 |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 탱크 수위 눈금을 가리킴 / 조수: 오른쪽 옆에서 클립보드(빈 줄무늬)를 들고 관 유량을 기록 / 초파리: 왼쪽에서 오른쪽을 보며 빠져나가는 관을 돋보기로 들여다봄 / 주판봇: 오른쪽에서 왼쪽을 보며 들어오는 관 앞에서 주판을 튕김 |
| 대체 글 (alt) | 밤의 연구실 물탱크 방에서 네 캐릭터가 세 갈래 관으로 드나드는 물과 어긋난 수위 눈금을 살피는 표지 |
| 앞 표지와 다른 점 | 시리즈 첫 표지 — 이후 표지는 물탱크 방을 피한다 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (기준: GitHub `adminmrobo/fruitfly-lab-expressions`).

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a water tank room inside the same night lab, a large glass water tank in the center connected to three pipes,
water level marks on the tank without numbers, purple lab light.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center pointing at the level marks on the tank;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the right side holding a clipboard with blank striped lines, watching the pipes;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, peering through a magnifying glass at the left pipe where water drains out;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, flicking abacus beads beside the right pipe where a strong stream of water flows in.
Visual metaphor of the topic: the left pipe drains water (reddish glow), the middle pipe drains a little (bluish glow), the right pipe pours a lot of water in (greenish glow); the painted level mark on the tank and the real water surface do not match.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
keep the bottom-left corner dark and simple; the light falls on the water tank.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

## 받은 뒤 반영

1. 16:9(±3%), 가로 1600 이상, 그림 속 글자 없음, 네 캐릭터 외형 확인
2. WebP 1600×900(220 KB 이하)으로 변환
3. `index.html`의 `<!-- lab-cover -->` … `<!-- /lab-cover -->` 사이 대체 표지를 `<picture>` 표지로 바꾼다 (SKILL 18-14-5). 그 밖의 본문은 바꾸지 않는다
4. 390·768·1280 폭에서 얼굴 잘림 확인
