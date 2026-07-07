import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="US Beauty Brand Research",
    page_icon="💄",
    layout="centered",
)

# HTML/CSS/JS를 별도 파일 없이 이 문자열에 직접 담아 렌더링합니다.
HTML_CONTENT = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>US Beauty Brand Research</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@400;600;700;800&family=Noto+Sans+KR:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; }
  :root {
    --princess-pink: #F9DEFF;
    --princess-blue: #CCD4FF;
    --princess-pink-deep: #e6a3f2;
    --princess-blue-deep: #9aa8ff;
    --princess-purple: #b98ff0;
    --bg-pink-light: #f3e2fd;
    --bg-blue-light: #d6ddfb;
    --text-dark: #3a2b57;
    --text-mid: #8a7aa8;
  }
  body {
    margin: 0;
    font-family: "Poppins", "Noto Sans KR", "Malgun Gothic", sans-serif;
    color: var(--text-dark);
    min-height: 100vh;
    background:
      radial-gradient(circle, rgba(255,255,255,0.75) 1.5px, transparent 1.8px) 0 0/30px 30px,
      linear-gradient(135deg, var(--bg-pink-light) 0%, var(--bg-blue-light) 100%);
    background-attachment: fixed;
    padding: 32px 16px 60px;
    position: relative;
    overflow-x: hidden;
  }
  .container {
    max-width: 780px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
  }
  .hero {
    text-align: center;
    margin-bottom: 28px;
  }
  .tiara-icon {
    width: 170px;
    height: auto;
    margin-bottom: 4px;
    filter: drop-shadow(0 3px 8px rgba(185, 143, 240, 0.4));
  }
  .hero h1 {
    font-family: "Dancing Script", "Poppins", cursive, sans-serif;
    font-weight: 700;
    font-size: clamp(36px, 8vw, 60px);
    margin: 0 0 10px;
    letter-spacing: 0.5px;
    background: linear-gradient(90deg, var(--princess-pink-deep), var(--princess-purple) 50%, var(--princess-blue-deep));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
  .hero p {
    font-size: clamp(13px, 2.4vw, 15px);
    color: var(--text-mid);
    max-width: 480px;
    margin: 0 auto;
    line-height: 1.55;
  }
  .glass-card {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid rgba(255, 255, 255, 0.8);
    border-radius: 26px;
    padding: 22px 22px;
    margin-bottom: 18px;
    box-shadow: 0 10px 34px rgba(185, 143, 240, 0.18);
  }
  .glass-card h2 {
    font-size: 15.5px;
    font-weight: 700;
    margin: 0 0 12px;
    color: var(--text-dark);
  }
  .glass-card h2 .emoji { margin-right: 6px; }
  label {
    display: block;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-mid);
    margin-bottom: 6px;
  }
  input[type=text] {
    width: 100%;
    padding: 12px 14px;
    border: 1.5px solid var(--princess-pink);
    background: #fff;
    border-radius: 14px;
    font-size: 14.5px;
    font-family: inherit;
    color: var(--text-dark);
    margin-bottom: 14px;
    outline: none;
    transition: border-color 0.15s;
  }
  input[type=text]:focus {
    border-color: var(--princess-purple);
  }
  button.cta {
    width: 100%;
    border: none;
    border-radius: 999px;
    padding: 14px 20px;
    font-size: 15.5px;
    font-weight: 700;
    font-family: inherit;
    color: #fff;
    cursor: pointer;
    background: linear-gradient(90deg, var(--princess-pink-deep), var(--princess-purple), var(--princess-blue-deep));
    box-shadow: 0 6px 18px rgba(185, 143, 240, 0.4);
    transition: transform 0.12s, box-shadow 0.12s;
  }
  button.cta:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 22px rgba(154, 168, 255, 0.45);
  }
  button.cta:active { transform: translateY(0); }
  .note {
    font-size: 11.5px;
    color: var(--text-mid);
    margin-top: 10px;
  }
  .status {
    color: var(--text-mid);
    font-size: 13px;
  }
  .channel-links {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  .channel-links a {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 9px 16px;
    background: #fff;
    border: 1.5px solid var(--princess-pink);
    border-radius: 999px;
    text-decoration: none;
    color: var(--text-dark);
    font-size: 13px;
    font-weight: 600;
  }
  .channel-links a:hover { background: #fdf3ff; }
  .brand-photo {
    width: 100%;
    max-height: 220px;
    object-fit: contain;
    background: #fff;
    border: 1.5px solid var(--princess-blue);
    border-radius: 18px;
    padding: 10px;
    margin-bottom: 16px;
    display: block;
  }
  .brand-photo-placeholder {
    width: 100%;
    height: 140px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 42px;
    background: linear-gradient(135deg, var(--princess-pink), var(--princess-blue));
    border-radius: 18px;
    margin-bottom: 16px;
  }
  .stat-row {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-bottom: 16px;
  }
  .stat-box {
    flex: 1;
    min-width: 150px;
    background: #fff;
    border: 1.5px solid var(--princess-blue);
    border-radius: 18px;
    padding: 14px 16px;
  }
  .stat-box .label {
    font-size: 11px;
    font-weight: 700;
    color: var(--princess-purple);
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 6px;
  }
  .stat-box .value {
    font-size: 15px;
    font-weight: 700;
    color: var(--text-dark);
  }
  .keyword-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 18px;
  }
  .keyword-tags span {
    background: linear-gradient(90deg, var(--princess-pink), var(--princess-blue));
    color: var(--text-dark);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 13px;
    border-radius: 999px;
  }
  .key-points {
    margin: 0;
    padding-left: 20px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .key-points li {
    font-size: 13.5px;
    line-height: 1.6;
    color: var(--text-dark);
  }
  .fallback-item {
    padding: 14px 16px;
    background: #fff;
    border: 1.5px solid var(--princess-pink);
    border-radius: 16px;
    font-size: 13.5px;
    line-height: 1.7;
  }
  .fallback-item .brand-list {
    color: var(--text-mid);
    font-size: 12.5px;
    margin-top: 6px;
  }
  .review-summary {
    font-size: 13.5px;
    line-height: 1.65;
    color: var(--text-dark);
    margin: 0;
  }
  .news-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .news-item {
    padding: 12px 14px;
    background: #fff;
    border: 1.5px solid var(--princess-blue);
    border-radius: 14px;
  }
  .news-item a {
    color: var(--princess-purple);
    text-decoration: none;
    font-size: 13.5px;
    font-weight: 700;
  }
  .news-item a:hover { text-decoration: underline; }
  .news-item .date {
    font-size: 11px;
    color: var(--text-mid);
    margin-top: 4px;
  }
  #resultsArea { display: none; }
  footer {
    text-align: center;
    font-size: 11.5px;
    color: var(--text-mid);
    margin-top: 24px;
  }
  @media (max-width: 480px) {
    body { padding: 24px 12px 40px; }
    .glass-card { padding: 18px 16px; border-radius: 18px; }
    .stat-box { min-width: 100%; }
  }
</style>
</head>
<body>
<div class="container">
  <div class="hero">
    <svg class="tiara-icon" viewBox="0 0 320 150" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <defs>
        <linearGradient id="tiaraGrad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" style="stop-color:var(--princess-pink-deep)"/>
          <stop offset="50%" style="stop-color:var(--princess-purple)"/>
          <stop offset="100%" style="stop-color:var(--princess-blue-deep)"/>
        </linearGradient>
      </defs>
      <path d="M10,128 Q160,146 310,128" fill="none" stroke="url(#tiaraGrad)" stroke-width="4.5" stroke-linecap="round"/>
      <path d="M16,120 Q160,136 304,120" fill="none" stroke="url(#tiaraGrad)" stroke-width="1.5" opacity="0.6"/>
      <path d="M20,122 L40,95 L60,122 L80,70 L100,122 L120,48 L140,122 L160,18 L180,122 L200,48 L220,122 L240,70 L260,122 L280,95 L300,122"
            fill="none" stroke="url(#tiaraGrad)" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
      <path d="M50,112 Q60,98 70,112" fill="none" stroke="url(#tiaraGrad)" stroke-width="1.8"/>
      <path d="M90,100 Q100,82 110,100" fill="none" stroke="url(#tiaraGrad)" stroke-width="1.8"/>
      <path d="M130,88 Q140,60 150,88" fill="none" stroke="url(#tiaraGrad)" stroke-width="1.8"/>
      <path d="M170,88 Q180,60 190,88" fill="none" stroke="url(#tiaraGrad)" stroke-width="1.8"/>
      <path d="M210,100 Q220,82 230,100" fill="none" stroke="url(#tiaraGrad)" stroke-width="1.8"/>
      <path d="M250,112 Q260,98 270,112" fill="none" stroke="url(#tiaraGrad)" stroke-width="1.8"/>
      <ellipse cx="160" cy="52" rx="8" ry="17" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.6"/>
      <ellipse cx="160" cy="52" rx="3" ry="10" fill="url(#tiaraGrad)" opacity="0.25"/>
      <circle cx="40" cy="95" r="3" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.1"/>
      <circle cx="80" cy="70" r="3.6" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.2"/>
      <circle cx="120" cy="48" r="4.2" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.3"/>
      <circle cx="160" cy="18" r="6.5" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.8"/>
      <circle cx="200" cy="48" r="4.2" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.3"/>
      <circle cx="240" cy="70" r="3.6" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.2"/>
      <circle cx="280" cy="95" r="3" fill="#fff" stroke="url(#tiaraGrad)" stroke-width="1.1"/>
      <circle cx="25" cy="124" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="45" cy="127" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="65" cy="129" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="95" cy="131" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="130" cy="132.5" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="160" cy="133" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="190" cy="132.5" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="225" cy="131" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="255" cy="129" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="275" cy="127" r="1.8" fill="url(#tiaraGrad)"/>
      <circle cx="295" cy="124" r="1.8" fill="url(#tiaraGrad)"/>
      <path d="M160,4 L163,10 L169,13 L163,16 L160,22 L157,16 L151,13 L157,10 Z" fill="#fff" opacity="0.95"/>
      <path d="M118,34 L120,38 L124,40 L120,42 L118,46 L116,42 L112,40 L116,38 Z" fill="#fff" opacity="0.85"/>
      <path d="M202,34 L204,38 L208,40 L204,42 L202,46 L200,42 L196,40 L200,38 Z" fill="#fff" opacity="0.85"/>
    </svg>
    <h1>US Beauty Brand Research</h1>
    <p>미국 뷰티 브랜드 100개를 담은 데이터베이스입니다. 브랜드명을 입력하면<br>포지셔닝, 평균 가격대, 키워드, 주요 포인트를 바로 확인할 수 있습니다.</p>
  </div>

  <div class="glass-card">
    <label>브랜드명 입력 (미국 브랜드)</label>
    <input type="text" id="keywordInput" list="brandOptions" placeholder="예: e.l.f. Cosmetics, Rare Beauty, CeraVe">
    <datalist id="brandOptions"></datalist>
    <button class="cta" id="generateBtn">브랜드 조회</button>
  </div>

  <div id="resultsArea">
    <div class="glass-card">
      <h3 style="margin:0 0 10px; font-size:13px; font-weight:600; color:var(--text-mid);">공식 채널 바로가기</h3>
      <div class="channel-links" id="channelLinks"></div>
      <div class="note">Instagram/TikTok 계정명은 브랜드명 기반 추정이라 실제 계정과 다를 수 있습니다.</div>
    </div>

    <div class="glass-card">
      <h2><span class="emoji">🏷️</span>브랜드 프로필</h2>
      <div id="profileContainer"><span class="status">브랜드명을 입력하고 "브랜드 조회"를 눌러주세요.</span></div>
    </div>

    <div class="glass-card">
      <h2><span class="emoji">⭐</span>리뷰 요약</h2>
      <div id="reviewContainer"><span class="status">브랜드명을 입력하고 "브랜드 조회"를 눌러주세요.</span></div>
    </div>

    <div class="glass-card">
      <h2><span class="emoji">📰</span>최근 뉴스</h2>
      <div id="newsContainer"><span class="status">브랜드명을 입력하고 "브랜드 조회"를 눌러주세요.</span></div>
      <div class="note">무료 뉴스 프록시를 사용해 실시간으로 불러옵니다. 간혹 느리거나 결과가 없을 수 있습니다.</div>
    </div>
  </div>

  <footer>미국 뷰티 브랜드 100종 데이터베이스 — 24종의 실제 리서치 데이터, 나머지 76종은 브랜드명을 제외한 세부 수치는 데모용 참고 데이터입니다.</footer>
</div>

<script>
  const BRAND_DB = [
    { name: "e.l.f. Cosmetics", heroProduct: "Halo Glow Liquid Filter", priceRange: "$5–$16",
      retailer: "Target, Ulta Beauty",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_6a011e78-7b38-4a83-9d32-170bf08be405?wid=300&hei=300&fmt=pjpeg",
      rating: "4.5/5 (9,994 reviews on Ulta Beauty)",
      reviewSummary: "가볍게 발리면서 자연스러운 '유리 피부' 광채를 내고 사롯 버벌리 유행의 가성비 좋은 대체하이템으로 호평받지만, 몇 시간 지나면 광채가 사라지고 번들거림으로 변한다는 불만도 자주 언급된다.",
      keywords: ["affordable", "cruelty-free & vegan", "drugstore/mass", "TikTok dupe favorite", "Gen Z"],
      keyPoints: [
        "이십억 대비 우수한 품질로 가성비 뷰티의 대명사로 불리며, 전체 제품의 약 75%가 10달러 이하로 가격 진입장벽이 매우 낮다.",
        "Leaping Bunny·PETA 인증을 받은 비건·크루얼티프리 브랜드로, 고가 인기 제품의 '대응(대체품)'으로 틱톡과 Z세대 사이에서 큰 인기를 얻고 있다.",
        "타겟, 얼타 등 매스 리테일 채널 통해 미국 전역에서 폭넓게 구매 가능하다."
      ] },
    { name: "Rare Beauty", heroProduct: "Soft Pinch Liquid Blush", priceRange: "$18–$32",
      retailer: "Sephora, Rare Beauty",
      imageUrl: "https://www.rarebeauty.com/cdn/shop/files/ECOMM-SP-LIQUID-BLUSH-DEWY-HOPE.jpg?format=pjpg&v=1762200490&width=1440",
      rating: "4.6/5 (21,300 reviews on Sephora)",
      reviewSummary: "손가락으로 톡톡 두드려 바르면 자연스러운 홍조가 오래 지속된다는 호평이 많지만, 팬베이스 이후 한번에 나오는 양이 많아 조절이 어렵고 건성 피부에는 뭉칠 수 있다는 지적도 있다.",
      keywords: ["Sephora exclusive", "mental health advocacy", "affordable luxury", "TikTok viral", "inclusive shade range"],
      keyPoints: [
        "셀레나 고메즈가 설립한 브랜드로, 판매 수익의 1%를 정신 건강 지원 기금(Rare Impact Fund)에 기부하며 자기 수용과 포용의 핵심 메시지로 내세운다.",
        "세포라 중심 유통 브랜드로 매스와 프레스티지 사이의 '합리적 럭셔리' 가격대를 형성하고 있다.",
        "소프트 핀치 리퀴드 블러셔가 틱톡에서 바이럴 히트를 기록하며 브랜드 대표 제품이자 세대를 넘어선 남성·Z세대의 필수템으로 자리잡았다."
      ] },
    { name: "Fenty Beauty", heroProduct: "Pro Filt'r Soft Matte Longwear Foundation", priceRange: "$20–$40",
      retailer: "Sephora, Fenty Beauty",
      imageUrl: "https://fentybeauty.com/cdn/shop/products/FB30006_FB0240_alt1.jpg?v=1762198551&width=1200",
      rating: "4.0/5 (17,400 reviews on Sephora)",
      reviewSummary: "50가지의 다양한 색상과 뛰어난 매트 지속력, 전부 조절력으로 진성 피부에서 좋은 평가를 받지만, 건성 피부에는 각질이 두드러지고 케이크처럼 뭉친다는 불만이 반복적으로 제기된다.",
      keywords: ["shade inclusivity", "Beauty for All", "celebrity-founded", "LVMH-backed", "prestige-adjacent"],
      keyPoints: [
        "리한나가 설립한 브랜드로 출시 당시 파운데이션 40개 색조를 선보이며 업계의 색조 포용성 기준을 완전히 바꿔놓았다.",
        "'Beauty for All'을 슬로건으로 모든 피부톤을 포용하는 철학을 지향하며, 매스보다 높고 프레스티지보다는 낮은 '어세서블 럭셔리' 가격대를 형성한다.",
        "LVMH 산하 셀럽 브랜드으로서 화제성을 발판으로 글로벌 프레스티지 유통망에서 강력한 입지를 갖췄다."
      ] },
    { name: "Kylie Cosmetics", heroProduct: "Kylie Lip Kit (Matte Liquid Lipstick + Lip Liner)", priceRange: "$14–$45",
      retailer: "Kylie Cosmetics, Ulta Beauty",
      imageUrl: "https://kyliecosmetics.com/cdn/shop/products/matte_lip_kit_bare.jpg?v=1741809265&width=1800",
      rating: "3.7/5 (4,814 reviews on Ulta Beauty)",
      reviewSummary: "선명한 발색과 트렌디한 컬러로 인기가 많지만, 제형이 건조하고 뻑뻑해지며 시간이 지나면 가장자리만 남고 얼룩덜룩하게 지워진다는 불만이 자주 나온다.",
      keywords: ["celebrity-founded", "social media-driven D2C", "glam makeup", "vegan (reformulated)", "sold-out hype"],
      keyPoints: [
        "카일리 제너가 립 키트(매트 리퀴드 립스틱+립 라이너) 하나로 시작해 1분 만에 완판되는 신화를 쓰며 급성장한 브랜드다.",
        "코티(Coty) 인수 이후 비건·클린 포뮬러로 재단장했으며, 강렬한 색조와 글래머러스한 메이크업 룩으로 유명하다.",
        "인스타그램·틱톡 등 소셜미디어와 인플루언서 마케팅에 기반을 둔 D2C 성공 사례로 꼽힌다."
      ] },
    { name: "Glossier", heroProduct: "Boy Brow", priceRange: "$14–$32",
      retailer: "Glossier, Sephora",
      imageUrl: "https://www.glossier.com/cdn/shop/files/glossier-boy-brow-black-carousel-01.png?v=1762200422",
      rating: "4.6/5 (25,571 ratings on Amazon)",
      reviewSummary: "자연스럽고 편안한 눈썹 연출과 오래가는 지속력으로 칭찬받아 밀레니얼 팬층을 형성했지만, 가격 대비 용량이 적고 오래 쓰면 뻑뻑해져 발림성이 떨어진다는 아쉬움도 있다.",
      keywords: ["skin-first minimalism", "millennial/Gen Z favorite", "DTC pioneer", "cult community", "no-makeup makeup look"],
      keyPoints: [
        "'피부가 먼저, 메이크업은 그다음'이라는 철학으로 자연스러운 노메이크업 룩을 지향한다.",
        "밀레니얼·Z세대를 겨냥한 미니멀 디자인과 친근한 톤의 브랜드로 강력한 컬트 팬덤을 구축했다.",
        "뷰티 블로그에서 출발해 인플루언서·직접 큐레이션된 콘텐츠 마케팅으로 성공한 대표적인 D2C 브랜드다."
      ] },
    { name: "Drunk Elephant", heroProduct: "Protini Polypeptide Firming Moisturizer", priceRange: "$26–$80",
      retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2588434",
      rating: "4.3/5 (3,675+ reviews on Amazon)",
      reviewSummary: "가볍지만 보습력이 뛰어난 피부 결과 탄력이 개선된다는 찬사를 받는 컬트 제품이지만, 일부 사용자는 트러블(브레이크아웃)이 생기거나 가격 대비 용량이 적다는 점을 아쉬워한다.",
      keywords: ["clean beauty", "biocompatible", "dermatologist-tested", "cruelty-free", "prestige skincare"],
      keyPoints: [
        "실리콘, 에센셜 오일, 인공 향료 등 자극 가능성이 있는 'Suspicious 6' 성분을 배제한 클린 뷰티일을 표방한다.",
        "피부와의 생체 친화성을 강조하며 임상적으로 검증된 활성 성분을 사용하는 프레스티지 스킨케어 브랜드다.",
        "인스타그래머와 인식된 이후에는 컬러풀한 패키지과 18~35세 소비자층 대상 브랜드 충성도를 유지하고 있다."
      ] },
    { name: "Kosas", heroProduct: "Revealer Concealer", priceRange: "$18–$42",
      retailer: "Sephora, Kosas.com",
      imageUrl: "https://kosas.com/cdn/shop/files/RC2024_01_vessel.jpg?v=1770932034&width=1920",
      rating: "4.5/5 (2,224+ reviews on Kosas.com)",
      reviewSummary: "크리미하고 이어한 발림성으로 다크서클을 자연스럽게 커버해준다는 호평이 많지만, 시간이 지나면 안이 크레이싱되거나 특정 주름에 낀다는 문제를 지적하는 리뷰도 있다.",
      keywords: ["clean beauty", "cruelty-free", "skincare-infused makeup", "TikTok viral", "Sephora bestseller"],
      keyPoints: [
        "스킨케어 성분과 메이크업을 결합한 클린 뷰티 브랜드로, 대표작 Revealer Concealer는 히알루론산과 카페인이 함유되어 다크서클 커버와 피부 케 개선을 동시에 제공한다.",
        "일론(하이엔리 비건 등)의 지지를 받은 틱톡에서 바이럴을 일으키며 세포라 베스트셀러 리스트에 꾸준히 이름을 올리고 있다."
      ] },
    { name: "Milk Makeup", heroProduct: "Hydro Grip Primer", priceRange: "$20–$38",
      retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2634881?w=600&h=600&fmt=auto",
      rating: "4.3/5 (8,695+ reviews on Amazon)",
      reviewSummary: "메이크업 밀착력과 지속력이 뛰어나고 이어한 젤 텍스처가 좋다는 평이 많지만, 일부 사용자는 트러블성 피부에 뾰루지가 올라온다는 불만을 제기한다.",
      keywords: ["clean beauty", "vegan", "cruelty-free", "Gen Z favorite", "dermatologist-tested"],
      keyPoints: [
        "뉴욕 감성의 젠더 뉴트럴·클린 뷰티 브랜드로, 대표작 Hydro Grip Primer는 히알루론산과 나이아신아마이드로 최대 12시간 지속력을 구현한다.",
        "2,500개 이상의 유해 성분을 배제한 비건·크루얼티프리 포뮬러를 내세우며, 실용적이고 미니멀한 이미지로 젊은 세대에게 인기가 높다."
      ] },
    { name: "Summer Fridays", heroProduct: "Jet Lag Mask", priceRange: "$24–$65",
      retailer: "Sephora, Summer Fridays",
      imageUrl: "https://summerfridays.com/cdn/shop/files/Jet-Lag-Main-Square.jpg?v=1720469004&width=1000",
      rating: "4.1/5 (162,000+ loves on Sephora)",
      reviewSummary: "쿠파한 텍스처가 건조한 피부에 즉각적인 수분감과 광채를 준다는 긍정적 반응이 많지만, 과도하게 바르면 밀리거나 모공 위에 남는다는 불만과 가격 대비 효과에 의문을 제기하는 리뷰도 있다.",
      keywords: ["celebrity-founded", "clean beauty", "hydration-focused", "Instagram/TikTok viral", "multi-use skincare"],
      keyPoints: [
        "인플루언서 마리안나 힐리스 리즈 굿맨이 공동 창립한 브랜드로, 대표작 Jet Lag Mask는 건조하고 지친 피부에 즉각적인 수분과 광채를 부여한다.",
        "복잡한 루틴 없이 누구든 쉽게 사용할 수 있는 멀티유즈 제품 구성으로 '인스타 럭셔리' 이미지를 구축했다."
      ] },
    { name: "Ilia Beauty", heroProduct: "Super Serum Skin Tint SPF 40", priceRange: "$24–$48",
      retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://iliabeauty.com/cdn/shop/files/Skyeppageimage_5450a883-1724-4b79-960c-26a3874d09fc.jpg?v=1710264865",
      rating: "4.5/5 (13,000+ reviews on iliabeauty.com)",
      reviewSummary: "가볍고 자연스러운 마무리와 다양한 색조 옵션을 갖춰 스킨케어와 메이크업의 둘 다를 해결한다는 호평이 많지만, 커버력이 약하고 시간이 지나면 유분기로 인해 번들거린다는 불만도 흔하다.",
      keywords: ["clean beauty", "vegan", "cruelty-free", "skin tint pioneer", "SPF-infused makeup"],
      keyPoints: [
        "클린 뷰티의 선도주자로, 대표작 Super Serum Skin Tint SPF 40은 세럼·미네랄 자외선 차단제·틴트 커버리지를 한 번에 해결하며 '스킨 헬스' 카테고리를 대중화시켰다.",
        "무향료, 무실리콘 등 까다로운 클린 포뮬 이서 기준을 지키면서도 다양한 뷰티 니즈를 아우른다."
      ] },
    { name: "Youth To The People", heroProduct: "Superfood Cleanser", priceRange: "$16–$58",
      retailer: "Sephora, Target",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_3c8e2dc5-0100-4a84-b221-bc88da8bc194?wid=300&hei=300&fmt=pjpeg",
      rating: "4.1/5 (7,000+ reviews on Sephora)",
      reviewSummary: "산뜻하면서도 메이크업과 노폐물을 깨끗하게 지워준다는 평이 많고 베스트셀러 클렌저로 꼽히지만, 세안 후 피부가 당기고 건조해진다는 불만이 반복적으로 제기된다.",
      keywords: ["vegan", "cruelty-free", "superfood ingredients", "cult favorite", "clinical-grade actives"],
      keyPoints: [
        "3대에 걸친 피부과학 전문성을 발판으로 케일, 시금치, 녹차 등 슈퍼푸드 추출물과 임상적으로 검증된 비건 액티브 성분을 결합한 클린 스킨케어 브랜드다.",
        "대표작 Superfood Cleanser는 상쾌한 젤 타입 클렌저이면서 메이크업 제거와 항산화 케어를 동시에 제공해 '컬트 클래식'으로 불린다."
      ] },
    { name: "First Aid Beauty", heroProduct: "Ultra Repair Cream", priceRange: "$14–$48",
      retailer: "Ulta Beauty, Target",
      imageUrl: "https://media.ulta.com/i/ulta/2295764?w=600&h=600&fmt=auto",
      rating: "4.6/5 (5,589 reviews on Ulta Beauty)",
      reviewSummary: "두꺼운 질감 크림이 건조하고 민감한 피부에 즉각적인 보습과 진정 효과를 준다는 찬사가 많지만, 일부는 발림성이 다소 무겁고 오트밀콜스 향이 민감한 피부에는 자극이 될 수 있다고 언급한다.",
      keywords: ["dermatologist-tested", "sensitive skin", "fragrance-free", "clinically proven", "steroid-free"],
      keyPoints: [
        "피부과 전문의 및 환자와의 협업을 통해 민감성 피부의 응급 케어에 특화된 브랜드로, 대표작 Ultra Repair Cream은 콜로이달 오트밀 성분으로 피부 장벽 개선 효과가 임상적으로 입증되었다.",
        "스테로이드 프리, 비건, 크루얼티프리 포뮬러를 강조하며 온 가족이 안심하고 사용할 수 있는 이미지를 갖고 있다."
      ] },
    { name: "CeraVe", heroProduct: "Moisturizing Cream", priceRange: "$8–$20",
      retailer: "Target, CVS",
      imageUrl: "https://www.cerave.com/-/media/project/loreal/brand-sites/cerave/americas/us/products-v4/moisturizing-cream/cerave_moisturizing_cream_16oz_jar_front-700x700-v3.jpg?rev=7e37e9cc45754615b1532d77df5a0b52",
      rating: "4.7/5 (16,700+ reviews on Ulta Beauty)",
      reviewSummary: "리뷰어들이 세라마이드와 히알루론산 배합의 건성/민감성 피부에 강력한 보습력을 제공하고 향이 없어 자극이 적다는 점을 가장 많이 칭찬한다. 다만 일부는 제형이 무겁고 발림성이 뻑뻑하며 여름철에 유분감이 느껴진다는 불만을 남긴다.",
      keywords: ["dermatologist-developed", "ceramides", "drugstore skincare", "fragrance-free", "barrier repair"],
      keyPoints: [
        "피부과 전문의들과 공동 개발한 브랜드로, 세라마이드와 히알루론산을 함유해 피부 장벽을 회복시키는 것이 핵심 강점이다.",
        "저렴한 드럭스토어 가격대에서 임상적으로 검증된 고기능 성분을 담은 미국 아마존 스킨케어 판매 1위를 차지할 만큼 폭넓은 대중적 신뢰를 얻고 있다."
      ] },
    { name: "Paula's Choice", heroProduct: "Skin Perfecting 2% BHA Liquid Exfoliant", priceRange: "$19–$50",
      retailer: "Sephora, Amazon",
      imageUrl: "https://www.paulaschoice.com/dw/image/v2/BBNX_PRD/on/demandware.static/-/Sites-pc-catalog/default/dw006e394e/images/products/2-percent-bha-liquid-exfoliant-2010-portrait.png?sw=2000&sfrm=png",
      rating: "4.4/5 (1,400+ reviews on Sephora)",
      reviewSummary: "모공 축소, 블랙헤드 개선, 피부결이 매끄러워지고 잔주름이 옅어졌다는 후기가 많은 꾸준히 재구매하는 사람이 많다. 반면 일부 민감성 피부 사용자는 초기에 발갛아지거나 건조함을 느꼈다는 불만을 남긴다.",
      keywords: ["science-backed", "cruelty-free", "fragrance-free", "ingredient transparency", "exfoliation experts"],
      keyPoints: [
        "창업자가 직접 성분의 과학적 근거를 검증하며 시작한 브랜드로, 인공 향료를 배제하고 임상 데이터에 기반한 처방을 고수한다.",
        "2% BHA 리퀴드 익스폴리언트는 모공 관리와 각질 케어의 대명사로 불리는 글로벌 베스트셀러다."
      ] },
    { name: "Supergoop!", heroProduct: "Unseen Sunscreen", priceRange: "$20–$48",
      retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2632648?w=500&h=500",
      rating: "4.7/5 (5,600+ reviews on Supergoop.com)",
      reviewSummary: "백탁 현상 없이 산뜻하게 발리고 메이크업 베이스로도 잘 어울린다는 호평이 압도적으로 많다. 다만 가격이 비싸고 일부 피부 타입에서는 필링(밀침) 현상이 있긴다는 불만이 종종 언급된다.",
      keywords: ["sun care specialist", "clean beauty", "reef-friendly claims", "everyday SPF", "makeup-gripping primer"],
      keyPoints: [
        "선케어에만 집중하는 프레스티지 브랜드로, 투명하고 향이 없는 텍스처로 매일 자외선 차단제를 바르는 습관을 대중화시켰다.",
        "선케어 겸 메이크업 프라이머 역할까지 겸하는 제품으로 입소문을 타며 브랜드에 대한 팬층이 두터웠다."
      ] },
    { name: "Tower 28 Beauty", heroProduct: "SOS Daily Rescue Facial Spray", priceRange: "$12–$28",
      retailer: "Sephora, Amazon",
      imageUrl: "https://www.tower28beauty.com/cdn/shop/files/SOS_20Spray_20_E2_80_94_C2_A04_20oz.webp?v=1762649181",
      rating: "4.8/5 (1,600+ reviews on Tower28beauty.com; also 9,000+ reviews on Sephora)",
      reviewSummary: "붉어짐과 자극을 빠르게 진정시켜 알레르기·민감성 피부에 효과적이라는 후기가 대부분이며 휴대하기 좋다는 점도 인기 요인이다. 다만 가격 대비 용량이 적고 특정 유럽산 같은 도시가 거슬린다는 불만도 꾸준히 나온다.",
      keywords: ["clean beauty", "sensitive skin", "fragrance-free", "vegan", "TikTok viral"],
      keyPoints: [
        "민감성·습진 피부도 사용할 수 있도록 미국 습진협회(NEA) 가이드라인을 100% 준수하는 저자극 클린 뷰티 브랜드다.",
        "차아염소산 성분의 SOS 스프레이는 즉각 효과로 틱톡에서 입소문이 나며 브랜드를 대표하는 히트 제품이 되었다."
      ] },
    { name: "Merit Beauty", heroProduct: "Shade Slick Tinted Lip Oil", priceRange: "$22–$46",
      retailer: "Sephora",
      imageUrl: "https://www.meritbeauty.com/cdn/shop/files/MERIT25-ShadeSlickSheen-Product_7ff61674-8d3e-4ad6-afc6-cf35f17e1105.jpg?v=1744400771",
      rating: "4.4/5 (750+ reviews on Sephora)",
      reviewSummary: "입술 케어가 되면서 색감이 이어하게 만들어주고 사용이 쉽다는 칭찬이 많다. 다만 오일 틴트 특성상 지속력이 짧아 자주 발라야 한다는 불만이 반복적으로 등장한다.",
      keywords: ["minimalist beauty", "clean beauty", "vegan", "cruelty-free", "five-minute routine"],
      keyPoints: [
        "'5분 완성 메이크업'을 컨셉트로, 적은 스텝과 절제된 컬러로 자연스러운 피부 표현을 추구하는 미니멀 뷰티 브랜드다.",
        "아이돌 셀레브리티 립 오일 쉐이드 슬릭은 세포라 클린 립글로스 부문 1위를 기록할 만큼 브랜드를 대표하는 히트 제품이다."
      ] },
    { name: "Haus Labs", heroProduct: "Triclone Skin Tech Foundation", priceRange: "$26–$52",
      retailer: "Sephora",
      imageUrl: "https://www.hauslabs.com/cdn/shop/files/HausLabs_4_silo_Foundation_Closed_230_4c53cd5d-53e7-4d99-a42b-6fafaf764107.png?v=1779230504",
      rating: "4.7/5 (13,900+ reviews on Haus Labs' website)",
      reviewSummary: "가볍고 자연스러운 커버력으로 하루 종일 지속되며 피부 톤이 균일해 보인다는 호평이 많다. 다만 일부 사용자는 몇 시간 지나면 파운데이션이 무너지거나 칙칙해진다는 불만을 제기한다.",
      keywords: ["vegan", "cruelty-free", "inclusive shade range", "skincare-infused makeup", "TikTok viral"],
      keyPoints: [
        "레이디 가가가 설립한 브랜드로, 발효 나이아신아마이드 등 스킨케어 성분을 메이크업에 접목한 '클린 아티스트리'를 지향한다.",
        "51가지 색조의 폭넓은 파운데이션 라인으로 포용성을 강조하며, 틱톡에서 대규모 조회수를 기록한 바이럴 히트 제품이다."
      ] },
    { name: "Morphe", heroProduct: "35O Supernatural Glow Eyeshadow Palette", priceRange: "$10–$50",
      retailer: "Ulta Beauty, Target",
      imageUrl: "https://m.media-amazon.com/images/I/711+Jvr4WpL._SL1500_.jpg",
      rating: "4.1/5 (290+ reviews on Ulta Beauty)",
      reviewSummary: "매트와 펄 아이섀도 모두 발색력이 뛰어나고 블렌딩이 쉽다는 호평이 많지만, 아이섀도 사용 시 파티클(fallout)이 많이 떨어진다는 불만이 자주 언급된다.",
      keywords: ["affordable prestige", "influencer-driven", "Gen Z favorite", "TikTok/YouTube viral", "trend-led color cosmetics"],
      keyPoints: [
        "유튜버·인플루언서와의 협업을 통해 급성장한 브랜드로, 가성비 좋은 대용량 아이섀도 팔레트와 브러시 세트로 유명하다.",
        "2030 초반 Z세대를 주요 타겟으로 일찍이 트렌드를 반영하고 다양한 컬러와 실험을 합리적인 가격에 제공하는 것이 강점이다."
      ] },
    { name: "Anastasia Beverly Hills", heroProduct: "Brow Wiz", priceRange: "$23–$45",
      retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2162560?w=500&h=500",
      rating: "4.4/5 (10,000+ reviews on Sephora)",
      reviewSummary: "가는 촉으로 눈썹 결이 자연스럽고 정밀하게 채울 수 있으며 지속력이 좋다는 평이 많지만, 다른 ABH 브로우 제품보다 블렌딩이 어렵고 있어 다소 진하게 나온다는 의견도 있다.",
      keywords: ["brow authority", "high pigmentation", "Instagram baking trend pioneer", "makeup artist favorite", "cult classic palettes"],
      keyPoints: [
        "Brow Wiz, Dipbrow Pomade 등 아이브로우 제품으로 '눈썹 정석시대'를 연 브랜드로, 브로우 카테고리의 표준으로 자리잡았다.",
        "Soft Glam, Norvina 시리즈 등 고발색 아이섀도 팔레트로도 유명하며 전문 메이크업 아티스트와 인플루언서들에게 폭넓게 사랑받는다."
      ] },
    { name: "Too Faced", heroProduct: "Better Than Sex Mascara", priceRange: "$12–$60",
      retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2263444",
      rating: "4.2/5 (24,459 reviews on Ulta Beauty)",
      reviewSummary: "풍성한 볼륨감과 극적인 속눈썹 연출, 부드러운 브러시를 칭찬하는 리뷰가 많지만, 일부 사용자는 뭉침(클럼핑)이나 번짐, 빨리 건조해지는 점을 단점으로 지적한다.",
      keywords: ["cruelty-free", "playful & feminine branding", "vegan-friendly options", "cult favorite", "accessible prestige"],
      keyPoints: [
        "발랄하고 여성스러운 브랜드 이미지와 재미있는 패키지 디자인으로 차별화되는 감성 마케팅에 특화됐다.",
        "전 세계에서 7초에 하나씩 팔린다는 베스트셀러 마스카라 Better Than Sex로 대표되며, 크루얼티프리 인증과 다양한 비건 옵션을 갖추고 있다."
      ] },
    { name: "Urban Decay", heroProduct: "Naked3 Eyeshadow Palette", priceRange: "$19–$59",
      retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2266731?w=500&h=500",
      rating: "4.6/5 (5,605 reviews on Ulta Beauty)",
      reviewSummary: "고운 색상의 핑크·브라운 계 아이섀도가 발색이 좋고 블렌딩이 쉬우며 오래 지속된다는 호평이 많지만, 일부 섀머 컬러(예: Dust)는 원하는 발색을 얻으려면 여러 번 겹쳐야 한다는 의견이 있다.",
      keywords: ["edgy/rebellious branding", "prestige beauty", "cult classic", "long-wear formulas", "L'Oréal Luxe portfolio"],
      keyPoints: [
        "'Beauty with an Edge'라는 슬로건 아래 반항적이고 감성 강한 브랜드 정체성을 구축한 프레스티지 브랜드다.",
        "누드 계 아이섀도의 대명사인 Naked 팔레트 시리즈는 출시 후 10억 달러 이상의 매출을 기록한 역대급 스테디셀러다."
      ] },
    { name: "NARS", heroProduct: "Orgasm Blush", priceRange: "$29–$54",
      retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://www.narscosmetics.com/dw/image/v2/BBSK_PRD/on/demandware.static/-/Sites-itemmaster_NARS/default/dw6b35594b/blush_medium/orgasmMedium.png?sw=395&sh=450&sm=fit",
      rating: "4.5/5 (1,053 reviews on Ulta Beauty)",
      reviewSummary: "은은한 골드 셔머가 도는 피치핑크 컬러가 다양한 피부톤에 잘 어울리고 최대 16시간 지속된다는 호평이 많지만, 발색력이 강해 과하게 바르면 부자연스러워 보일 수 있다는 의견도 있다.",
      keywords: ["French chic", "makeup artist heritage", "iconic pigmentation", "organic word-of-mouth buzz", "cult status"],
      keyPoints: [
        "프랑스 출신 메이크업 아티스트 프랑수아 나스가 1994년 설립한 브랜드로, 세련된 프리지즘 감성과 전문 아티스트의 시각 노하우가 특징이다.",
        "1999년 출시된 시그니처 블러셔 Orgasm은 별도의 마케팅 없이 입소문만으로 25년 넘게 미국 판매 1위 블러셔 자리를 지키고 있다."
      ] },
    { name: "Clinique", heroProduct: "Dramatically Different Moisturizing Lotion+", priceRange: "$13–$68",
      retailer: "Ulta Beauty, Macy's",
      imageUrl: "https://media.ulta.com/i/ulta/2261902?w=500&h=500",
      rating: "4.5/5 (9,318 reviews on Ulta Beauty)",
      reviewSummary: "산뜻한 사용감과 8시간 지속되는 보습력으로 건성·복합성 피부에 좋다는 평이 많지만, 지성 피부에는 다소 무겁고 번들거린다는 불만이 흔하게 제기된다.",
      keywords: ["dermatologist-developed", "allergy-tested", "fragrance-free", "hypoallergenic", "3-Step skincare system"],
      keyPoints: [
        "1968년 피부과 전문의와 공동 개발한 세계 최초의 알러지 테스트 완료·향료 무첨가 브랜드로, 민감성 피부도 안심하고 쓸 수 있는 저자극 포뮬러로 신뢰받는다.",
        "대표 제품인 Dramatically Different Moisturizing Lotion+은 전 세계에서 6초에 하나씩 팔리는 브랜드 최고 베스트셀러다."
      ] },

    // ---- 아래 76개는 데모용 가상 데이터입니다 (브랜드명은 실존, 세부 수치는 참고용으로 임의 작성) ----
    { name: "Maybelline New York", heroProduct: "Great Lash Mascara", priceRange: "$6–$13", retailer: "Target, CVS",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_29161a86-ad85-4a51-966f-ba5bfc6a0418?wid=300&hei=300&fmt=pjpeg",
      rating: "4.3/5 (8,200+ reviews, 참고용)", reviewSummary: "저렴한 가격에 자연스러운 볼륨감을 준다는 평이 많지만 뭉침 현상을 지적하는 리뷰도 있다.",
      keywords: ["drugstore icon", "mass affordable", "mascara heritage", "photo-ready"],
      keyPoints: ["1971년 출시 이후 지금까지 사랑받는 드럭스토어 마스카라의 대명사로, 가성비와 대중적 인지도가 가장 큰 강점이다."] },
    { name: "Revlon", heroProduct: "ColorStay Foundation", priceRange: "$13–$18", retailer: "Target, Walmart",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_9e62743d-a66a-43f5-9b32-e019fbda47d1?wid=300&hei=300&fmt=pjpeg",
      rating: "4.2/5 (6,500+ reviews, 참고용)", reviewSummary: "지속력은 좋지만 건성 피부에는 다시 매트하고 무겁게 느껴질 수 있다는 의견이 있다.",
      keywords: ["24-hour wear", "drugstore staple", "full coverage", "classic formula"],
      keyPoints: ["24시간 지속력을 내세운 파운데이션으로 오랫동안 드럭스토어 풀커버리지의 기준으로 자리잡았다."] },
    { name: "CoverGirl", heroProduct: "Clean Fresh Foundation", priceRange: "$10–$15", retailer: "Target, Walmart",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_5b09648e-503e-4357-a061-54acd15741f1?wid=300&hei=300&fmt=pjpeg",
      rating: "4.0/5 (3,000+ reviews, 참고용)", reviewSummary: "가볍고 자연스러운 마무리가 장점이지만 커버력이 다소 약하다는 후기가 있다.",
      keywords: ["mass market", "clean beauty (mass)", "classic American brand", "cruelty-free"],
      keyPoints: ["미국을 대표하는 매스 메이크업 브랜드로 접근성과 대중적 신뢰도가 강점이다."] },
    { name: "Wet n Wild", heroProduct: "MegaLast Liquid Catsuit High-Shine Lipstick", priceRange: "$3–$6", retailer: "Ulta Beauty, Target",
      imageUrl: "https://media.ulta.com/i/ulta/2539290",
      rating: "4.4/5 (5,000+ reviews, 참고용)", reviewSummary: "가격 대비 발색과 지속력이 훌륭하다는 평이 압도적이다.",
      keywords: ["ultra affordable", "viral dupes", "Gen Z favorite", "cruelty-free"],
      keyPoints: ["3~5달러대 이하 가격의 고발색 립스틱을 선보이며 SNS에서 '가성비 갓' 제품으로 자주 언급된다."] },
    { name: "NYX Professional Makeup", heroProduct: "Butter Gloss", priceRange: "$6–$12", retailer: "Ulta Beauty, Target",
      imageUrl: "https://media.ulta.com/i/ulta/2268533",
      rating: "4.5/5 (10,000+ reviews, 참고용)", reviewSummary: "부드러운 발림성과 다양한 색상이 장점으로 꼽힌다.",
      keywords: ["makeup artist approved", "affordable prestige", "bold color range", "cruelty-free"],
      keyPoints: ["메이크업 아티스트들 사이에서는 인정받는 합리적인 가격의 색조 전문 브랜드다."] },
    { name: "Physicians Formula", heroProduct: "Butter Bronzer", priceRange: "$12–$16", retailer: "Ulta Beauty, Walmart",
      imageUrl: "https://media.ulta.com/i/ulta/2294340",
      rating: "4.3/5 (4,000+ reviews, 참고용)", reviewSummary: "자연스러운 태닝 컬러가 장점이지만 일부 섀도는 발색이 과하다는 의견도 있다.",
      keywords: ["dermatologist-developed", "hypoallergenic", "drugstore bronzer icon", "cruelty-free"],
      keyPoints: ["피부과 전문의 감수로 개발된 저자극 포뮬러를 내세우는 드럭스토어 브랜드다."] },
    { name: "Almay", heroProduct: "Clear Complexion Concealer", priceRange: "$9–$14", retailer: "Target, Walmart",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_87327f38-ce56-4ba8-b02f-12f1096f86dd?wid=300&hei=300&fmt=pjpeg",
      rating: "4.1/5 (2,500+ reviews, 참고용)", reviewSummary: "순한 사용감은 좋지만 커버력이 약하다는 불만이 있다.",
      keywords: ["hypoallergenic", "fragrance-free", "sensitive skin friendly", "classic drugstore"],
      keyPoints: ["민감성 피부를 위한 저자극 포뮬러로 오래 신뢰를 쌓아온 브랜드다."] },
    { name: "Milani Cosmetics", heroProduct: "Baked Blush", priceRange: "$9–$13", retailer: "Target, Ulta Beauty",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_0ac940ab-e4aa-4d7f-9333-6e96e29cf994?wid=300&hei=300&fmt=pjpeg",
      rating: "4.6/5 (7,000+ reviews, 참고용)", reviewSummary: "저렴한 가격에 자연스러운 발색이 장점으로 꼽힌다.",
      keywords: ["affordable Italian-inspired", "cult blush", "drugstore bestseller", "cruelty-free"],
      keyPoints: ["이탈리안 뷰티에서 영감을 받은 베이크드 블러셔로 드럭스토어 컬트힛으로 자리잡았다."] },
    { name: "L.A. Girl Cosmetics", heroProduct: "Pro Conceal HD Concealer", priceRange: "$5–$8", retailer: "Target, Walmart",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_589e933f-f992-45c5-a154-23ef1071e43f?wid=300&hei=300&fmt=pjpeg",
      rating: "4.4/5 (3,000+ reviews, 참고용)", reviewSummary: "가성비는 훌륭하지만 색상 매칭이 다소 어렵다는 의견이 있다.",
      keywords: ["ultra affordable", "high pigment", "TikTok viral", "LA-based"],
      keyPoints: ["저렴한 가격에 높은 커버력을 앞세워 SNS에서 자주 추천되는 컨실러 브랜드다."] },
    { name: "Neutrogena", heroProduct: "Hydro Boost Water Gel", priceRange: "$15–$22", retailer: "Target, CVS",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_83cbb31a-b7ef-43b5-84ba-a28df85a25ec?wid=300&hei=300&fmt=pjpeg",
      rating: "4.6/5 (20,000+ reviews, 참고용)", reviewSummary: "가볍고 빠르게 흡수되는 수분감이 장점으로 자주 언급된다.",
      keywords: ["dermatologist-recommended", "hyaluronic acid", "drugstore skincare leader", "fragrance-free options"],
      keyPoints: ["히알루론산 기반의 워터 젤 모이스처라이저로 드럭스토어 스킨케어의 베스트셀러로 꼽힌다."] },
    { name: "Olay", heroProduct: "Regenerist Micro-Sculpting Cream", priceRange: "$20–$30", retailer: "Target, Walmart",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_14f215e0-1d99-41e8-b662-a3df74b1e9e9?wid=300&hei=300&fmt=pjpeg",
      rating: "4.5/5 (15,000+ reviews, 참고용)", reviewSummary: "탄력 개선 효과가 좋다는 평이 많지만 일부는 향이 강하다고 느낀다.",
      keywords: ["anti-aging drugstore leader", "peptide complex", "dermatologist-tested", "mass prestige"],
      keyPoints: ["펩타이드 성분을 담은 안티에이징 크림으로 드럭스토어 프레스티지 스킨케어를 대표한다."] },
    { name: "Aveeno", heroProduct: "Daily Moisturizing Lotion", priceRange: "$8–$14", retailer: "Target, Walmart",
      imageUrl: "https://target.scene7.com/is/image/Target/GUEST_078aa80c-3858-4e4e-a908-296911922429?wid=300&hei=300&fmt=pjpeg",
      rating: "4.7/5 (18,000+ reviews, 참고용)", reviewSummary: "가볍고 순한 사용감이 장점으로 꼽히며 온 가족이 함께 쓸 수 있다는 호평이 많다.",
      keywords: ["oat-based formula", "dermatologist recommended", "sensitive skin", "drugstore staple"],
      keyPoints: ["콜로이달 오트밀 성분으로 민감성 피부에도 안심 보습 로션으로 오랜 신뢰를 받는다."] },
    { name: "bareMinerals", heroProduct: "Original Loose Powder Foundation", priceRange: "$34–$40", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2093947",
      rating: "4.3/5 (9,000+ reviews, 참고용)", reviewSummary: "가볍고 자연스러운 마무리가 장점이지만 커버력 조절이 익숙해지기까지 시간이 걸린다는 의견이 있다.",
      keywords: ["mineral makeup pioneer", "clean formula", "skin-friendly", "San Francisco-based"],
      keyPoints: ["미네랄 파운데이션 카테고리를 대중화시킨 색조 브랜드로 꼽힌다."] },
    { name: "Smashbox Cosmetics", heroProduct: "Photo Finish Primer", priceRange: "$20–$38", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2233964",
      rating: "4.4/5 (12,000+ reviews, 참고용)", reviewSummary: "메이크업 밀착력이 좋다는 평이 많지만 실리콘 베이스라 무거울 수 있다는 의견도 있다.",
      keywords: ["studio/photography heritage", "LA-based", "primer pioneer", "long-wear formulas"],
      keyPoints: ["사진 스튜디오에서 시작된 브랜드답게 포토제닉 파이니시와 프라이머로 유명하다."] },
    { name: "Benefit Cosmetics", heroProduct: "Hoola Bronzer", priceRange: "$32–$36", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2595640",
      rating: "4.6/5 (25,000+ reviews, 참고용)", reviewSummary: "자연스러운 태닝 표현이 장점이지만 오렌지 지빛이 난다는 일부 의견도 있다.",
      keywords: ["playful branding", "brow bar heritage", "SF-based", "cult bronzer"],
      keyPoints: ["발랄한 브랜딩과 눈썹 전문성으로 유명하며, 훌라 브론저는 자연스러운 태닝 컬러의 대명사다."] },
    { name: "Stila Cosmetics", heroProduct: "Stay All Day Liquid Lipstick", priceRange: "$22–$26", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2632938",
      rating: "4.3/5 (5,000+ reviews, 참고용)", reviewSummary: "발색과 지속력은 좋지만 텍스처가 건조하다는 의견이 있다.",
      keywords: ["long-wear color", "cult liquid lipstick", "LA-based", "cruelty-free"],
      keyPoints: ["스테이 올 데이 리퀴드 립스틱은 지속력 좋은 립 제품의 스테디셀러로 꼽힌다."] },
    { name: "Laura Mercier Cosmetics", heroProduct: "Translucent Setting Powder", priceRange: "$30–$38", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2559917",
      rating: "4.7/5 (10,000+ reviews, 참고용)", reviewSummary: "메이크업을 자연스럽게 고정해준다는 호평이 많다.",
      keywords: ["makeup artist heritage", "setting powder icon", "prestige beauty", "flawless finish"],
      keyPoints: ["트랜스루일트 세팅 파우더는 메이크업 아티스트들이 가장 많이 찾는 세팅 제품 중 하나로 꼽힌다."] },
    { name: "Hourglass Cosmetics", heroProduct: "Ambient Lighting Powder", priceRange: "$46–$52", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2575863",
      rating: "4.6/5 (7,000+ reviews, 참고용)", reviewSummary: "가격은 높지만 피부를 뽀샤시하게 만들어준다는 찬사가 많다.",
      keywords: ["luxury LA brand", "vegan formulas", "soft-focus finish", "prestige highlighter"],
      keyPoints: ["앰비언트 라이팅 파우더는 은은한 광채를 주는 하이라이팅 파우더의 대명사로 꼽힌다."] },
    { name: "Tarte Cosmetics", heroProduct: "Shape Tape Concealer", priceRange: "$18–$32", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2501218",
      rating: "4.4/5 (30,000+ reviews, 참고용)", reviewSummary: "커버력은 뛰어나지만 건성 피부에는 다시 무겁다는 의견이 있다.",
      keywords: ["cult concealer", "vegan/cruelty-free", "high coverage", "NY-based"],
      keyPoints: ["쉐이프 테이프 컨실러는 출시 이후 꾸준히 히트 되는 컬트 컨실러다."] },
    { name: "IT Cosmetics", heroProduct: "CC+ Cream", priceRange: "$22–$48", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2264064",
      rating: "4.5/5 (18,000+ reviews, 참고용)", reviewSummary: "커버력과 보습력을 동시에 잡았다는 평이 많다.",
      keywords: ["dermatologist co-developed", "QVC success story", "color-correcting", "prestige-drugstore crossover"],
      keyPoints: ["CC+ 크림은 스킨케어와 커버리지를 결합한 제품으로 브랜드의 대표작으로 꼽힌다."] },
    { name: "Josie Maran Cosmetics", heroProduct: "Whipped Argan Oil Body Butter", priceRange: "$18–$38", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://www.josiemaran.com/cdn/shop/files/PDP-BodyButter-Core-Wirecutter_260cf1ad-e15c-427e-9f9e-e76dcff7679f.png?v=1774381452",
      rating: "4.5/5 (4,000+ reviews, 참고용)", reviewSummary: "보습력이 뛰어나다는 평이 많지만 향이 호불호가 있다.",
      keywords: ["argan oil pioneer", "clean beauty", "cruelty-free", "multi-tasking formulas"],
      keyPoints: ["아르간 오일을 뷰티 업계에 대중화시킨 브랜드로 유명하다."] },
    { name: "BECCA Cosmetics", heroProduct: "Shimmering Skin Perfector (Smashbox x BECCA)", priceRange: "$18–$38", retailer: "Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2587487?w=500&h=500",
      rating: "4.6/5 (9,000+ reviews, 참고용)", reviewSummary: "화사한 광채 효과가 뛰어나다는 찬사가 많다.",
      keywords: ["highlighter pioneer", "glow-focused", "vegan-friendly", "cult status"],
      keyPoints: ["셔머링 스킨 퍼펙터는 하이라이터 카테고리를 재정의했다는 평가를 받는 제품이다."] },
    { name: "Estée Lauder", heroProduct: "Advanced Night Repair Serum", priceRange: "$58–$135", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2568523?w=500&h=500",
      rating: "4.7/5 (14,000+ reviews, 참고용)", reviewSummary: "피부 결 개선 효과가 뛰어나다는 평이 많지만 가격대가 높다는 의견도 있다.",
      keywords: ["luxury skincare icon", "anti-aging heritage", "global prestige", "clinical research"],
      keyPoints: ["어드밴스드 나이트 리페어는 전 세계에서 4초에 하나씩 팔린다는 브랜드의 시그니처 세럼이다."] },
    { name: "Bobbi Brown Cosmetics", heroProduct: "Vitamin Enriched Face Base", priceRange: "$30–$44", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2583728?w=500&h=500",
      rating: "4.4/5 (5,000+ reviews, 참고용)", reviewSummary: "이어한 베이스 프라이머로 좋은 평가를 받는다.",
      keywords: ["natural makeup pioneer", "makeup artist heritage", "prestige beauty", "skin-first philosophy"],
      keyPoints: ["자연스러운 '노 메이크업 메이크업' 룩을 대중화시킨 브랜드로 꼽힌다."] },
    { name: "Origins", heroProduct: "GinZing Energy-Boosting Moisturizer", priceRange: "$20–$38", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2552852?w=500&h=500",
      rating: "4.5/5 (6,000+ reviews, 참고용)", reviewSummary: "산뜻한 사용감과 생기 부여 효과가 좋다는 평이 많다.",
      keywords: ["botanical ingredients", "energizing skincare", "Estée Lauder family", "cruelty-free"],
      keyPoints: ["진저 모이스처라이저는 식물성 카페인 성분으로 즉각적인 생기를 주는 제품으로 유명하다."] },
    { name: "Tatcha", heroProduct: "The Dewy Skin Cream", priceRange: "$35–$80", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://tatcha.com/cdn/shop/files/DewySkinCream-pdp-FullSize-MainImg-1200x1200_dcc7d73a-8daf-4ddd-83e2-6fb74c789720.jpg?v=1766157508&width=2048",
      rating: "4.6/5 (8,000+ reviews, 참고용)", reviewSummary: "수분감과 광채가 뛰어나다는 평이 많지만 가격이 높다는 의견도 있다.",
      keywords: ["Japanese-inspired skincare", "San Francisco-based", "luxury clean beauty", "hydration-focused"],
      keyPoints: ["듀이 스킨 크림은 이어하고 광채나는 피부를 만들어주는 브랜드의 대표작이다."] },
    { name: "Kiehl's", heroProduct: "Midnight Recovery Concentrate", priceRange: "$27–$72", retailer: "Kiehl's, Ulta Beauty",
      imageUrl: "https://www.kiehls.com/dw/image/v2/AAFM_PRD/on/demandware.static/-/Sites-kiehls-master-catalog/default/dw5b5f90cd/nextgen/skin-care/face-serums-and-oils/midnight-recovery/midnight-recovery-concentrate/2025/Kiehls_US_2024_MR-Concentrate-Oil_PDP_Packshot_100ML_2400x2400.png",
      rating: "4.6/5 (10,000+ reviews, 참고용)", reviewSummary: "자고 일어나면 피부가 편안해진다는 호평이 많다.",
      keywords: ["apothecary heritage since 1851", "NYC-founded", "science-backed formulas", "minimal packaging"],
      keyPoints: ["미드나잇 리커버리 컨센트레이트는 브랜드를 대표하는 페이스 오일로 꼽힌다."] },
    { name: "Fresh", heroProduct: "Rose Deep Hydration Face Cream", priceRange: "$52–$68", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2584147?w=500&h=500",
      rating: "4.5/5 (5,000+ reviews, 참고용)", reviewSummary: "이어함과 은은한 장미향이 장점으로 꼽힌다.",
      keywords: ["Boston-founded", "botanical luxury", "rose-based skincare", "sensorial textures"],
      keyPoints: ["로즈 딥 하이드레이션 크림은 브랜드의 시그니처 장미 성분을 담은 대표 제품이다."] },
    { name: "Philosophy", heroProduct: "Purity Made Simple Cleanser", priceRange: "$16–$28", retailer: "Ulta Beauty, QVC",
      imageUrl: "https://media.ulta.com/i/ulta/2565512?w=500&h=500",
      rating: "4.5/5 (9,000+ reviews, 참고용)", reviewSummary: "산뜻하면서도 깨끗하게 지워준다는 평이 많다.",
      keywords: ["Arizona-founded", "simple skincare philosophy", "inspirational branding", "cruelty-free"],
      keyPoints: ["퓨리티 메이드 심플 클렌저는 브랜드의 베스트셀러 3-in-1 클렌저다."] },
    { name: "StriVectin", heroProduct: "Tightening Neck Cream", priceRange: "$59–$99", retailer: "Ulta Beauty, Dermstore",
      imageUrl: "https://strivectin.com/cdn/shop/files/TL_AdvancedTightening_NeckCream_PLUS_1.7oz_1440x1440_300dpi_ALT_PDP_01.jpg?v=1757983780",
      rating: "4.4/5 (3,000+ reviews, 참고용)", reviewSummary: "목주름 개선 효과가 좋다는 후기가 많다.",
      keywords: ["neck & body-focused", "peptide technology", "clinical anti-aging", "US-founded"],
      keyPoints: ["타이트닝 넥 크림은 넥 케어 카테고리를 개척한 제품으로 유명하다."] },
    { name: "Dermalogica", heroProduct: "Daily Microfoliant", priceRange: "$20–$66", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://www.dermalogica.com/cdn/shop/files/01_DailyMicCampaign_PDP_benefits_Tile01.jpg?v=1762197961",
      rating: "4.7/5 (7,000+ reviews, 참고용)", reviewSummary: "부드럽게 각질을 제거해준다는 호평이 많다.",
      keywords: ["professional skincare heritage", "LA-founded", "esthetician-favorite", "science-based"],
      keyPoints: ["데일리 마이크로폴리언트는 전문 에스테틱 업계에서도 신뢰받는 각질 제거제다."] },
    { name: "Murad", heroProduct: "Rapid Dark Spot Correcting Serum", priceRange: "$34–$92", retailer: "Ulta Beauty",
      imageUrl: "https://www.murad.com/cdn/shop/files/831900_RDSCS_2026_Carousel1_Soldier.png?v=1775512868",
      rating: "4.4/5 (4,000+ reviews, 참고용)", reviewSummary: "잡티 개선 효과가 좋다는 평이 많다.",
      keywords: ["dermatologist-founded", "LA-based", "clinical skincare", "anti-aging focus"],
      keyPoints: ["피부과 전문의가 설립한 브랜드로, 색소침착 개선 세라이 대표 제품이다."] },
    { name: "Sunday Riley", heroProduct: "Good Genes Lactic Acid Treatment", priceRange: "$56–$122", retailer: "Sephora",
      imageUrl: "https://sundayriley.com/cdn/shop/files/Subheading_4.png?v=1758920489",
      rating: "4.5/5 (6,000+ reviews, 참고용)", reviewSummary: "즉각적인 피부 톤 개선 효과가 좋다는 찬사가 많다.",
      keywords: ["NYC-founded", "cult skincare", "clinical actives", "luxury exfoliants"],
      keyPoints: ["굿 지느스는 즉각적인 광채 효과로 유명한 브랜드의 시그니처 세럼이다."] },
    { name: "Herbivore Botanicals", heroProduct: "Bakuchiol Retinol Alternative Serum", priceRange: "$18–$58", retailer: "Sephora",
      imageUrl: "https://www.herbivorebotanicals.com/cdn/shop/files/Bakuchiol_FaceSerum_4x5_Carousel_1_22bf443e-9622-4530-8702-3273c3eab8ab.png?v=1765998409",
      rating: "4.3/5 (3,000+ reviews, 참고용)", reviewSummary: "자극 없이 순하게 사용할 수 있다는 평이 많다.",
      keywords: ["Seattle-founded", "plant-based formulas", "clean beauty", "minimalist packaging"],
      keyPoints: ["바쿠치올 세럼은 레티놀 대체 성분으로 유명한 클린 뷰티 브랜드의 대표작이다."] },
    { name: "Glow Recipe", heroProduct: "Watermelon Glow Niacinamide Dew Drops", priceRange: "$19–$40", retailer: "Sephora",
      imageUrl: "https://www.glowrecipe.com/cdn/shop/files/10_21_2410_21_24_WM_DEWDROPS-_1.jpg?v=1762197997",
      rating: "4.6/5 (20,000+ reviews, 참고용)", reviewSummary: "이어하고 즉각적인 광채 효과가 뛰어나다는 호평이 많다.",
      keywords: ["Korean-American founders", "NY-based", "fruit-inspired skincare", "TikTok viral"],
      keyPoints: ["워터멜론 글로우 드롭스는 즉각적인 광채를 주는 브랜드의 대표 히트 제품이다."] },
    { name: "Peach & Lily", heroProduct: "Glass Skin Refining Serum", priceRange: "$19–$48", retailer: "Ulta Beauty, Target",
      imageUrl: "https://media.ulta.com/i/ulta/2532640",
      rating: "4.4/5 (2,500+ reviews, 참고용)", reviewSummary: "피부결 개선 효과가 좋다는 평이 많다.",
      keywords: ["Korean-American founder", "NY-based", "K-beauty curation", "glass skin trend pioneer"],
      keyPoints: ["글래스 스킨 리파이닝 세럼은 '유리 피부' 트렌드를 대중화시킨 브랜드의 대표 제품이다."] },
    { name: "Then I Met You", heroProduct: "Living Cleansing Balm", priceRange: "$16–$32", retailer: "Sephora, Soko Glam",
      imageUrl: "https://sokoglam.com/cdn/shop/files/Then-I-Met-You_Living-Cleansing-Balm.jpg?v=1753227792",
      rating: "4.6/5 (3,000+ reviews, 참고용)", reviewSummary: "메이크업을 부드럽게 녹여준다는 호평이 많다.",
      keywords: ["Korean-American founder Charlotte Cho", "double cleansing ritual", "minimalist skincare", "clean formulas"],
      keyPoints: ["리빙 클렌징 밤은 브랜드를 대표하는 첫 번째 클렌징 제품이다."] },
    { name: "Versed", heroProduct: "Guards Up Daily Mineral Sunscreen SPF 35", priceRange: "$12–$20", retailer: "Target", imageUrl: null,
      rating: "4.3/5 (5,000+ reviews, 참고용)", reviewSummary: "백탁 없이 산뜻하게 발린다는 평이 많다.",
      keywords: ["Target-exclusive clean beauty", "accessible pricing", "vegan formulas", "transparency-focused"],
      keyPoints: ["타겟 스킨 메드 션 산라인 저 근접 가능한 가격의 클린 선케어로 인기를 얻고 있다."] },
    { name: "Naturium", heroProduct: "Niacinamide Serum", priceRange: "$16–$25", retailer: "Ulta Beauty, Target",
      imageUrl: "https://naturium.com/cdn/shop/files/NATR_NiacinamideSerum_Anniv_Front_CapOn_ecomm.webp?v=1774292312",
      rating: "4.5/5 (10,000+ reviews, 참고용)", reviewSummary: "가성비 좋은 액티브 성분으로 호평받는다.",
      keywords: ["LA-founded by Susan Yara", "affordable actives", "clinical ingredients", "TikTok viral"],
      keyPoints: ["나이아신아마이드 세럼은 합리적인 가격에 고농도 활성 성분을 담아 인기를 얻고 있다."] },
    { name: "Kopari Beauty", heroProduct: "Coconut Melt", priceRange: "$15–$32", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://koparibeauty.com/cdn/shop/files/OGMelt.png?v=1762198102&width=1024",
      rating: "4.4/5 (3,000+ reviews, 참고용)", reviewSummary: "보습력이 뛰어나다는 평이 많다.",
      keywords: ["San Diego-founded", "coconut-based formulas", "clean beauty", "multi-use products"],
      keyPoints: ["코코넛 멜트는 다용도로 쓸 수 있는 코코넛 오일 제품으로 브랜드의 시그니처다."] },
    { name: "Saie Beauty", heroProduct: "Slip Tint", priceRange: "$18–$32", retailer: "Sephora",
      imageUrl: "https://saiehello.com/cdn/shop/products/saie-slip-tint-2022-featured-1_1200x1200.png?v=1667320864",
      rating: "4.5/5 (5,000+ reviews, 참고용)", reviewSummary: "자연스러운 피부 표현이 장점으로 꼽힌다.",
      keywords: ["LA-founded", "clean beauty minimalism", "skin tint pioneer", "sustainable packaging"],
      keyPoints: ["슬립 틴트는 가볍고 자연스러운 커버리지로 브랜드의 대표 제품이 되었다."] },
    { name: "Vacation Inc.", heroProduct: "Classic Whip Sunscreen SPF 30", priceRange: "$10–$22", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2596247?w=600&h=600&fmt=auto",
      rating: "4.3/5 (2,000+ reviews, 참고용)", reviewSummary: "향과 텍스처가 독특하고 재미있다는 평이 많다.",
      keywords: ["retro branding", "nostalgic sunscreen", "clean formulas", "playful marketing"],
      keyPoints: ["레트로 컨셉의 선스크린 브랜드로 SNS에서 화제를 모으고 있다."] },
    { name: "Rhode Skin", heroProduct: "Peptide Lip Treatment", priceRange: "$16–$29", retailer: "Sephora",
      imageUrl: "https://www.rhodeskin.com/cdn/shop/files/main-png-2000x2000_unscented_480x480.png?v=1705598678",
      rating: "4.5/5 (8,000+ reviews, 참고용)", reviewSummary: "이어하고 은은한 광채를 준다는 호평이 많다.",
      keywords: ["Hailey Bieber's brand", "minimalist skincare", "viral DTC", "clean beauty"],
      keyPoints: ["펩타이드 립 트리트먼트는 출시와 동시에 화제를 일으킨 브랜드의 대표작이다."] },
    { name: "Item Beauty", heroProduct: "Brow Chow", priceRange: "$12–$22", retailer: null, imageUrl: null,
      rating: "4.1/5 (1,500+ reviews, 참고용)", reviewSummary: "자연스러운 눈썹 표현이 장점으로 꼽힌다.",
      keywords: ["Addison Rae's brand", "Gen Z-focused", "clean formulas", "TikTok-driven"],
      keyPoints: ["브로우 차우는 Z세대를 겨냥한 브랜드의 대표 브로우 제품이다."] },
    { name: "About-Face", heroProduct: "Line Artist Gel Eyeliner", priceRange: "$12–$20", retailer: "Ulta Beauty", imageUrl: null,
      rating: "4.2/5 (1,200+ reviews, 참고용)", reviewSummary: "발색이 좋고 지속력이 있다는 평이 많다.",
      keywords: ["Halsey's brand", "bold color range", "vegan/cruelty-free", "inclusive marketing"],
      keyPoints: ["라인 아티스트 아이라이너는 다양한 컬러로 브랜드의 감성을 보여주는 제품이다."] },
    { name: "r.e.m. beauty", heroProduct: "Sweet Dreams Eyeshadow Quad", priceRange: "$20–$36", retailer: "Ulta Beauty", imageUrl: null,
      rating: "4.0/5 (1,000+ reviews, 참고용)", reviewSummary: "발색은 좋지만 파티클이 많이 떨어진다는 의견도 있다.",
      keywords: ["Ariana Grande's brand", "space-inspired branding", "vegan formulas", "Gen Z favorite"],
      keyPoints: ["앤 셀러 칼라 팔레트는 브랜드의 우주 컨셉을 담은 대표 아이섀도 제품이다."] },
    { name: "KVD Beauty", heroProduct: "Tattoo Liner", priceRange: "$10–$22", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2624745cm_alt01",
      rating: "4.5/5 (15,000+ reviews, 참고용)", reviewSummary: "얇고 정교한 라인 표현이 장점으로 꼽힌다.",
      keywords: ["Kat Von D's brand", "tattoo-inspired precision", "vegan/cruelty-free", "bold artistry"],
      keyPoints: ["타투 라이너는 정밀한 필으로 아이라이너 카테고리의 스테디셀러가 되었다."] },
    { name: "Jouer Cosmetics", heroProduct: "Sunswept Bronzer Duo", priceRange: "$18–$34", retailer: "Ulta Beauty", imageUrl: null,
      rating: "4.3/5 (2,500+ reviews, 참고용)", reviewSummary: "이어하고 자연스러운 발림성이 좋다는 평이 많다.",
      keywords: ["LA-based", "French-inspired branding", "cream-based makeup", "cruelty-free"],
      keyPoints: ["프렌치 감성의 자연스러운 태닝 컬러를 표현하는 브랜드의 대표 제품이다."] },
    { name: "ColourPop Cosmetics", heroProduct: "Super Shock Shadow", priceRange: "$8–$14", retailer: "Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2569217?w=600&h=600&fmt=auto",
      rating: "4.4/5 (9,000+ reviews, 참고용)", reviewSummary: "가성비와 발색력이 뛰어나다는 평이 많다.",
      keywords: ["ultra affordable prestige", "LA-based", "trendy collabs", "vegan/cruelty-free"],
      keyPoints: ["슈퍼 샥 아이섀도는 크리미한 텍스처와 저렴한 가격으로 인기를 끄는 대표 아이섀도다."] },
    { name: "Juvia's Place", heroProduct: "The Nubian Eyeshadow Palette", priceRange: "$18–$28", retailer: "Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2536106",
      rating: "4.6/5 (4,000+ reviews, 참고용)", reviewSummary: "다양한 피부톤에 잘 어울리는 발색력이 장점으로 꼽힌다.",
      keywords: ["Nigerian-American founder", "NY-based", "richly pigmented for deep skin tones", "affordable prestige"],
      keyPoints: ["뉴비안 팔레트는 진한 피부톤에도 선명하게 발색되는 대표 팔레트다."] },
    { name: "Fenty Skin", heroProduct: "Fat Water Toner Serum", priceRange: "$28–$34", retailer: "Sephora",
      imageUrl: "https://fentybeauty.com/cdn/shop/products/47151.jpg?format=webp&v=1762198050&width=800",
      rating: "4.3/5 (3,000+ reviews, 참고용)", reviewSummary: "산뜻한 수분감이 좋다는 평이 많다.",
      keywords: ["Rihanna's skincare line", "inclusive skincare", "clean formulas", "sister brand to Fenty Beauty"],
      keyPoints: ["팻 워터 토너 세럼은 결합한 브랜드의 시그니처 제품이다."] },
    { name: "Kulfi Beauty", heroProduct: "Main Match Concealer", priceRange: "$18–$28", retailer: "Sephora", imageUrl: null,
      rating: "4.4/5 (800+ reviews, 참고용)", reviewSummary: "은은한 광채 효과가 좋다는 평이 많다.",
      keywords: ["South Asian-focused clean beauty", "cultural heritage ingredients", "inclusive shade ranges", "NY-based"],
      keyPoints: ["사우스 아시아 마스크는 남아시아 전통 성분을 현대적으로 재해석한 브랜드의 대표작이다."] },
    { name: "Topicals", heroProduct: "Faded Serum", priceRange: "$16–$36", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://cdn.shopify.com/s/files/1/0503/2932/1627/files/251009_TOPICALS_Website_Faded_OG_Ppage_1_1.jpg?v=1773429615&width=348&height=470&crop=center",
      rating: "4.5/5 (5,000+ reviews, 참고용)", reviewSummary: "색소침착 개선 효과가 좋다는 호평이 많다.",
      keywords: ["chronic skin condition focus", "LA-based", "clean formulas", "inclusive branding"],
      keyPoints: ["페이디드 세럼은 색소침착과 튼 케어에 특화된 브랜드의 대표 제품이다."] },
    { name: "Beautyblender", heroProduct: "The Original Beautyblender Sponge", priceRange: "$20–$22", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2530759",
      rating: "4.7/5 (30,000+ reviews, 참고용)", reviewSummary: "매끄러운 베이스 표현이 가능하다는 압도적인 호평을 받는다.",
      keywords: ["makeup tool pioneer", "LA-based", "egg-shaped sponge icon", "professional makeup artist favorite"],
      keyPoints: ["오리지널 뷰티블렌더는 스펀지 메이크업 도구 카테고리를 정의한 아이콘 제품이다."] },
    { name: "Wander Beauty", heroProduct: "Baggage Claim Eye Mask", priceRange: "$15–$29", retailer: "Sephora",
      imageUrl: "https://www.wanderbeauty.com/cdn/shop/products/BaggageClaimRoseGoldEyeMasks_BCRF1_d0a582e9-3b8d-49e8-a785-1c12633ef736.jpg?v=1756998950&width=650",
      rating: "4.4/5 (2,000+ reviews, 참고용)", reviewSummary: "즉각적인 눈가 리프레시 효과가 좋다는 평이 많다.",
      keywords: ["travel-inspired branding", "NY-based", "multi-tasking beauty", "on-the-go formulas"],
      keyPoints: ["배기지 클레임 아이마스크는 여행 중에도 사용하기 좋은 브랜드의 대표작이다."] },
    { name: "Danessa Myricks Beauty", heroProduct: "Yummy Skin Blurring Balm", priceRange: "$14–$36", retailer: "Sephora",
      imageUrl: "https://danessamyricksbeauty.com/cdn/shop/files/BBP_C_S_0.5.jpg?v=1739472500",
      rating: "4.6/5 (4,000+ reviews, 참고용)", reviewSummary: "자연스러운 피부 표현이 뛰어나다는 호평이 많다.",
      keywords: ["makeup artist-founded", "NY-based", "skin-blurring innovation", "inclusive shade range"],
      keyPoints: ["여미 스킨 블러링 밤은 스킨케어와 메이크업을 결합한 브랜드의 대표 제품이다."] },
    { name: "Pat McGrath Labs", heroProduct: "Skin Fetish Highlighter", priceRange: "$38–$82", retailer: "Sephora",
      imageUrl: "https://cdn.shopify.com/s/files/1/1463/9662/files/PMG_PDP_Passion_Fleur_Highlighter_Balm_Duo-Cyber_Lotus_OPEN_d6796dc5-32c3-4eac-93d6-0f94a166db89.jpg?v=1721858038",
      rating: "4.7/5 (5,000+ reviews, 참고용)", reviewSummary: "고급스러운 광채 효과가 뛰어나다는 찬사가 많다.",
      keywords: ["celebrity makeup artist brand", "NYC-based", "luxury pigmentation", "editorial-inspired"],
      keyPoints: ["스킨 페티시 하이라이터는 화려한 광채로 브랜드를 대표하는 하이라이터다."] },
    { name: "Makeup By Mario", heroProduct: "Soft Sculpt Bronzer", priceRange: "$32–$36", retailer: "Sephora",
      imageUrl: "https://www.makeupbymario.com/cdn/shop/files/MBM_SSBB_OPEN_PACK_LIGHT.jpg?v=1747064670&width=640",
      rating: "4.5/5 (6,000+ reviews, 참고용)", reviewSummary: "자연스러운 음영 표현이 장점으로 꼽힌다.",
      keywords: ["celebrity makeup artist brand", "LA-based", "sculpting expertise", "editorial-inspired"],
      keyPoints: ["소프트 스컬프트 브론저는 자연스러운 윤곽 표현으로 브랜드를 대표하는 제품이다."] },
    { name: "Fourth Ray Beauty", heroProduct: "Rainfall 2% Hyaluronic Acid Serum", priceRange: "$15–$28", retailer: "Ulta Beauty", imageUrl: null,
      rating: "4.3/5 (2,000+ reviews, 참고용)", reviewSummary: "가벼운 텍스처와 수분 공급 효과가 좋다는 평이 많다.",
      keywords: ["influencer-founded (KathleenLights)", "DTC skincare", "affordable actives", "playful branding"],
      keyPoints: ["레인폴 히알루론산 세럼은 브랜드의 대표 수분 세럼이다."] },
    { name: "Dose of Colors", heroProduct: "Liquid Matte Lipstick", priceRange: "$16–$18", retailer: "Dose of Colors, Ulta Beauty",
      imageUrl: "https://doseofcolors.com/cdn/shop/files/LIQUID_MATTE_BOTTLE_-_TRUFFLE_V1.jpg?v=1726258664&width=420",
      rating: "4.4/5 (3,000+ reviews, 참고용)", reviewSummary: "발색과 지속력이 뛰어나다는 평이 많다.",
      keywords: ["LA-based", "influencer-founded", "bold pigmentation", "long-wear formulas"],
      keyPoints: ["리퀴드 매트 립스틱은 강렬한 발색으로 브랜드를 대표하는 립 제품이다."] },
    { name: "Dr. Dennis Gross Skincare", heroProduct: "Alpha Beta Universal Daily Peel", priceRange: "$22–$88", retailer: "Sephora, Dr. Dennis Gross",
      imageUrl: "https://www.drdennisgross.com/dw/image/v2/BBSK_PRD/on/demandware.static/-/Sites-itemmaster_ddg/default/dw0dfd6292/2026/April/UniversalPeel/UNI_DailyPeel_960x1150_1.jpg",
      rating: "4.6/5 (10,000+ reviews, 참고용)", reviewSummary: "즉각적인 피부결 개선 효과가 좋다는 호평이 많다.",
      keywords: ["dermatologist-founded", "NYC-based", "at-home peel pioneer", "clinical skincare"],
      keyPoints: ["알파 베타 유니버설 데일리 필은 홈 필링 카테고리를 대중화시킨 브랜드의 대표작이다."] },
    { name: "Peace Out Skincare", heroProduct: "Acne Healing Dots", priceRange: "$12–$28", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2606805",
      rating: "4.5/5 (7,000+ reviews, 참고용)", reviewSummary: "빠른 트러블 진정 효과가 좋다는 평이 많다.",
      keywords: ["LA-based", "targeted skincare patches", "clean formulas", "problem-solving focus"],
      keyPoints: ["여드름 힐링 패치는 트러블 케어 카테고리를 대중화시킨 브랜드의 대표 제품이다."] },
    { name: "Bliss", heroProduct: "Fab Foaming 2-in-1 Cleanser & Exfoliator", priceRange: "$16–$24", retailer: "Ulta Beauty, Bliss World",
      imageUrl: "https://www.blissworld.com/cdn/shop/files/FabFoamingCleanser2_1.jpg?v=1776104495&width=1946",
      rating: "4.4/5 (4,000+ reviews, 참고용)", reviewSummary: "산뜻한 세정력이 좋다는 평이 많다.",
      keywords: ["NYC spa heritage", "playful branding", "clean formulas", "affordable spa experience"],
      keyPoints: ["팹 폼잉 클렌저는 스파 헤리티지를 담은 브랜드의 클렌징 제품이다."] },
    { name: "Osea Malibu", heroProduct: "Undaria Algae Body Oil", priceRange: "$22–$68", retailer: "Osea Malibu, Sephora",
      imageUrl: "https://osea.imgix.net/files/OSEA_UndariaAlgaeBodyOil_UAO-295-DTC-1_badgeless.jpg?v=1758087570&auto=format,compress&w=720",
      rating: "4.7/5 (5,000+ reviews, 참고용)", reviewSummary: "이어하고 은은한 광채를 준다는 찬사가 많다.",
      keywords: ["Malibu-based", "ocean-derived ingredients", "clean beauty", "cult body care"],
      keyPoints: ["언다리아 알지 바디 오일은 브랜드를 대표하는 컬트 바디케어 제품이다."] },
    { name: "Beekman 1802", heroProduct: "Pure Goat Milk Whipped Body Cream", priceRange: "$18–$38", retailer: "Ulta Beauty, Beekman 1802",
      imageUrl: "https://media.ulta.com/i/ulta/2613282",
      rating: "4.5/5 (3,000+ reviews, 참고용)", reviewSummary: "순하고 이어한 사용감이 장점으로 꼽힌다.",
      keywords: ["upstate NY farm heritage", "goat milk skincare", "clean formulas", "wholesome branding"],
      keyPoints: ["고트 밀크 크림은 브랜드의 시그니처 성분을 담은 대표 모이스처라이저다."] },
    { name: "Truly Beauty", heroProduct: "Unicorn Fruit Body Butter", priceRange: "$18–$26", retailer: "Ulta Beauty, Truly Beauty",
      imageUrl: "https://www.trulybeauty.com/cdn/shop/files/UNICORNFRUIT_WhippedBodyButter_6oz_NEWFRENCH_pink_V5_1_1500X1875_crop_center.jpg?v=1762323515",
      rating: "4.2/5 (4,000+ reviews, 참고용)", reviewSummary: "향과 보습력이 좋다는 평이 많지만 텍스처가 무겁다는 의견도 있다.",
      keywords: ["DTC body care", "playful branding", "TikTok viral", "cruelty-free"],
      keyPoints: ["유니콘 프루트 바디 버터는 SNS에서 입소문난 브랜드의 대표 바디케어 제품이다."] },
    { name: "Function of Beauty", heroProduct: "Custom Hair Mask", priceRange: "$20–$36", retailer: "Function of Beauty (direct-to-consumer)",
      imageUrl: "https://functionofbeauty.com/cdn/shop/files/Mask_Sky_Blue_Reflection.png?v=1744744527",
      rating: "4.3/5 (6,000+ reviews, 참고용)", reviewSummary: "개인 맞춤 포뮬러 효과가 좋다는 평이 많다.",
      keywords: ["personalized beauty pioneer", "DTC subscription model", "customizable formorms", "vegan options"],
      keyPoints: ["커스텀 헤어 마스크는 개인 맞춤형 뷰티를 대중화시킨 브랜드의 대표 제품이다."] },
    { name: "Buxom Cosmetics", heroProduct: "Full-On Plumping Lip Cream", priceRange: "$22–$24", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2299249",
      rating: "4.5/5 (8,000+ reviews, 참고용)", reviewSummary: "입술이 통통해 보이는 효과가 좋다는 호평이 많다.",
      keywords: ["Portland-based", "plumping lip pioneer", "bold pigmentation", "cult lip gloss"],
      keyPoints: ["풀온 플럼핑 립 크림은 볼륨 립글로스 카테고리의 스테디셀러다."] },
    { name: "e.l.f. Skin", heroProduct: "Holy Hydration! Face Cream", priceRange: "$12–$16", retailer: "Ulta Beauty, Target",
      imageUrl: "https://media.ulta.com/i/ulta/2563564",
      rating: "4.4/5 (5,000+ reviews, 참고용)", reviewSummary: "가성비 좋은 보습력으로 호평받는다.",
      keywords: ["affordable skincare", "sister brand to e.l.f. Cosmetics", "clean formulas", "TikTok viral"],
      keyPoints: ["홀리 하이드레이션 크림은 저렴한 가격의 고보습 크림으로 인기를 얻고 있다."] },
    { name: "Kate Somerville", heroProduct: "ExfoliKate Intensive Exfoliating Treatment", priceRange: "$32–$95", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2531096",
      rating: "4.5/5 (6,000+ reviews, 참고용)", reviewSummary: "즉각적인 광채 효과가 좋다는 찬사가 많다.",
      keywords: ["LA celebrity facialist brand", "cult exfoliant", "clinical skincare", "red-carpet favorite"],
      keyPoints: ["엑스폴리케이트는 레드카펫 셀럽들이 애용하는 브랜드의 대표 각질 제거제다."] },
    { name: "GlamGlow", heroProduct: "Supermud Clearing Treatment", priceRange: "$23–$69", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2570372",
      rating: "4.4/5 (10,000+ reviews, 참고용)", reviewSummary: "모공 정화 효과가 좋다는 평이 많지만 건조함을 느낀다는 의견도 있다.",
      keywords: ["LA-based", "celebrity-favorite mask", "intensive treatments", "Estée Lauder family"],
      keyPoints: ["슈퍼머드는 브랜드를 대표하는 클레이 마스크로 모공 관리에 특화되어 있다."] },
    { name: "Ouai", heroProduct: "Detox Shampoo", priceRange: "$15–$32", retailer: "Sephora, Ulta Beauty",
      imageUrl: "https://media.ulta.com/i/ulta/2565432",
      rating: "4.4/5 (7,000+ reviews, 참고용)", reviewSummary: "두피가 가벼워진다는 호평이 많다.",
      keywords: ["celebrity hairstylist-founded (Jen Atkin)", "LA-based", "minimalist branding", "hair & body crossover"],
      keyPoints: ["디톡스 샴푸는 브랜드를 대표하는 헤어 케어 제품이다."] },
    { name: "Live Tinted", heroProduct: "Huestick Multitasking Color", priceRange: "$18–$22", retailer: "Ulta Beauty, Target",
      imageUrl: "https://media.ulta.com/i/ulta/2588675",
      rating: "4.3/5 (1,500+ reviews, 참고용)", reviewSummary: "다양한 피부톤에 맞는 색상 범위가 장점으로 꼽힌다.",
      keywords: ["South Asian founder Deepica Mutyala", "NY-based", "inclusive shade ranges", "multi-use products"],
      keyPoints: ["휴스틱은 다양한 피부톤을 위한 멀티스틱으로 브랜드의 대표 제품이다."] },
    { name: "Half Magic Beauty", heroProduct: "Chromaddiction Shimmer/Matte Eye Paint", priceRange: "$24–$28", retailer: "Ulta Beauty", imageUrl: null,
      rating: "4.2/5 (900+ reviews, 참고용)", reviewSummary: "독특하고 화려한 컬러 표현이 장점으로 꼽힌다.",
      keywords: ["LA-based", "avant-garde color cosmetics", "makeup artist-founded", "bold experimental shades"],
      keyPoints: ["크로마딕션 컬러 드롭스는 실험적인 컬러 메이크업으로 유명한 브랜드의 대표작이다."] },
    { name: "Coola Suncare", heroProduct: "Classic Face Sunscreen SPF 30", priceRange: "$18–$36", retailer: "Ulta Beauty, Sephora",
      imageUrl: "https://media.ulta.com/i/ulta/2272546",
      rating: "4.5/5 (6,000+ reviews, 참고용)", reviewSummary: "산뜻한 사용감과 자연 유래 성분이 장점으로 꼽힌다.",
      keywords: ["San Diego-based", "organic sunscreen pioneer", "clean beauty", "reef-friendly formulas"],
      keyPoints: ["클래식 페이스 선스크린은 유기농 성분 기반 선케어의 대표 제품이다."] },
    { name: "Alba Botanica", heroProduct: "Hawaiian Coconut Milk Body Cream", priceRange: "$8–$14", retailer: "Walmart, Target",
      imageUrl: "https://i5.walmartimages.com/seo/Alba-Botanica-Coconut-Milk-Body-Cream-6-5-oz_4b9fd841-cdae-4f86-8216-bfc3c56da5a2_1.559f2100cc965341f93b544733053055.jpeg",
      rating: "4.6/5 (5,000+ reviews, 참고용)", reviewSummary: "부드러운 보습감과 은은한 향이 장점으로 꼽힌다.",
      keywords: ["natural ingredients pioneer", "Hawaiian-inspired formulas", "cruelty-free", "affordable clean beauty"],
      keyPoints: ["하와이안 코코넛 밀크 바디 크림은 자연 유래 성분 기반 바디케어의 스테디셀러다."] }
  ];

  function normalize(str) {
    return str.toLowerCase().replace(/[^a-z0-9]/g, "");
  }

  function findBrand(query) {
    const nq = normalize(query);
    if (!nq) return null;
    return BRAND_DB.find(b => {
      const nb = normalize(b.name);
      return nb === nq || nb.includes(nq) || nq.includes(nb);
    }) || null;
  }

  const datalist = document.getElementById("brandOptions");
  BRAND_DB.forEach(b => {
    const opt = document.createElement("option");
    opt.value = b.name;
    datalist.appendChild(opt);
  });

  function renderChannelLinks(brand) {
    const container = document.getElementById("channelLinks");
    const handle = brand.replace(/\s+/g, "").toLowerCase();
    const links = [
      { icon: "🌐", label: "공식 홈페이지", url: `https://www.google.com/search?q=${encodeURIComponent(brand + " official website")}&btnI=1` },
      { icon: "📷", label: "Instagram", url: `https://www.instagram.com/${encodeURIComponent(handle)}/` },
      { icon: "🎵", label: "TikTok", url: `https://www.tiktok.com/@${encodeURIComponent(handle)}` },
      { icon: "▶️", label: "YouTube", url: `https://www.youtube.com/results?search_query=${encodeURIComponent(brand)}` }
    ];
    container.innerHTML = "";
    links.forEach(l => {
      const a = document.createElement("a");
      a.href = l.url;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.innerHTML = `${l.icon} ${l.label}`;
      container.appendChild(a);
    });
  }

  function renderProfile(brandData) {
    const container = document.getElementById("profileContainer");
    const keywordTags = brandData.keywords.map(k => `<span>${k}</span>`).join("");
    const keyPointItems = brandData.keyPoints.map(p => `<li>${p}</li>`).join("");
    const photoHtml = brandData.imageUrl
      ? `<img class="brand-photo" src="${brandData.imageUrl}" alt="${brandData.heroProduct}" onerror="this.replaceWith(Object.assign(document.createElement('div'), {className:'brand-photo-placeholder', textContent:'🧴'}))">`
      : `<div class="brand-photo-placeholder">🧴</div>`;
    container.innerHTML = `
      ${photoHtml}
      <div class="stat-row">
        <div class="stat-box">
          <div class="label">Hero Product</div>
          <div class="value">${brandData.heroProduct}</div>
        </div>
        <div class="stat-box">
          <div class="label">Price Range</div>
          <div class="value">${brandData.priceRange}</div>
        </div>
        <div class="stat-box">
          <div class="label">Where to Buy</div>
          <div class="value">${brandData.retailer || "정보 없음"}</div>
        </div>
      </div>
      <div class="keyword-tags">${keywordTags}</div>
      <ul class="key-points">${keyPointItems}</ul>
    `;
  }

  function renderNotFound(brand) {
    const container = document.getElementById("profileContainer");
    const names = BRAND_DB.map(b => b.name).join(", ");
    container.innerHTML = `
      <div class="fallback-item">
        "${brand}"은(는) 아직 데이터베이스에 없는 브랜드입니다.
        <div class="brand-list">현재 지원 브랜드: ${names}</div>
      </div>
    `;
  }

  function renderReview(brandData) {
    const container = document.getElementById("reviewContainer");
    if (!brandData.rating && !brandData.reviewSummary) {
      container.innerHTML = `<span class="status">아직 리뷰 데이터가 없습니다.</span>`;
      return;
    }
    container.innerHTML = `
      <div class="stat-row">
        <div class="stat-box">
          <div class="label">Rating</div>
          <div class="value">${brandData.rating}</div>
        </div>
      </div>
      <p class="review-summary">${brandData.reviewSummary}</p>
    `;
  }

  function renderReviewEmpty() {
    document.getElementById("reviewContainer").innerHTML =
      `<span class="status">브랜드를 조회하면 리뷰 요약이 여기에 표시됩니다.</span>`;
  }

  const NEWS_TIMEOUT_MS = 5000;
  const newsCache = new Map();

  async function fetchNewsItems(query) {
    const rssUrl = `https://news.google.com/rss/search?q=${encodeURIComponent(query)}&hl=en-US&gl=US&ceid=US:en`;
    const proxyUrl = `https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(rssUrl)}`;
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), NEWS_TIMEOUT_MS);
    try {
      const res = await fetch(proxyUrl, { signal: controller.signal });
      const data = await res.json();
      if (data.status === "ok" && data.items && data.items.length > 0) return data.items;
      return null;
    } finally {
      clearTimeout(timer);
    }
  }

  function renderNewsList(items) {
    const container = document.getElementById("newsContainer");
    const list = document.createElement("div");
    list.className = "news-list";
    items.slice(0, 6).forEach(item => {
      const div = document.createElement("div");
      div.className = "news-item";
      const dateStr = item.pubDate ? item.pubDate.slice(0, 16) : "";
      div.innerHTML = `<a href="${item.link}" target="_blank" rel="noopener noreferrer">${item.title}</a><div class="date">${dateStr}</div>`;
      list.appendChild(div);
    });
    container.innerHTML = "";
    container.appendChild(list);
  }

  function renderNewsFallback(brand) {
    const container = document.getElementById("newsContainer");
    const searchUrl = `https://news.google.com/search?q=${encodeURIComponent(brand)}&hl=en`;
    container.innerHTML = `<div class="fallback-item">"${brand}" 관련 최근 뉴스를 찾지 못했습니다. <a href="${searchUrl}" target="_blank" rel="noopener noreferrer">Google 뉴스에서 직접 확인하기</a></div>`;
  }

  async function renderNews(brand) {
    const container = document.getElementById("newsContainer");

    if (newsCache.has(brand)) {
      const cached = newsCache.get(brand);
      if (cached) renderNewsList(cached);
      else renderNewsFallback(brand);
      return;
    }

    container.innerHTML = '<span class="status">뉴스를 불러오는 중... (최대 5초)</span>';
    let items = null;
    try {
      items = await fetchNewsItems(brand);
    } catch (e) {
      items = null;
    }
    newsCache.set(brand, items);
    if (items) {
      renderNewsList(items);
    } else {
      renderNewsFallback(brand);
    }
  }

  function showResults() {
    const brandRaw = document.getElementById("keywordInput").value;
    const brand = brandRaw && brandRaw.trim() ? brandRaw.trim() : "";

    if (!brand) {
      alert("브랜드명을 입력해주세요.");
      return;
    }

    document.getElementById("resultsArea").style.display = "block";
    renderChannelLinks(brand);
    renderNews(brand);

    const brandData = findBrand(brand);
    if (brandData) {
      renderProfile(brandData);
      renderReview(brandData);
    } else {
      renderNotFound(brand);
      renderReviewEmpty();
    }
  }

  document.getElementById("generateBtn").addEventListener("click", showResults);
  document.getElementById("keywordInput").addEventListener("keydown", (e) => {
    if (e.key === "Enter") showResults();
  });
</script>
</body>
</html>
"""

components.html(HTML_CONTENT, height=1400, scrolling=True)
