# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:30:15 2020

@author: seongjin.son
"""

#하루
import re
pattern1=re.compile(r"""(\s*<<.*>>)?
                    (\s*\[.*\])?
                    (\s*□.*)
                    (\s*-.*)\s*
                    (\s*-.*)\s*""",re.VERBOSE)



#패턴 1 색출

pattern1=re.compile(r'\n\[.*\].*',re.VERBOSE)
index1=pattern1.findall(data)[0]
index2=pattern1.findall(data)[1]

start_index=data.find(index1)
end_index=data.find(index2)
print(data[start_index:end_index])

def get_from_index():
    

pattern1=re.compile(r'\n\[.*\].*',re.VERBOSE)

print(pattern1.findall(data))



#패턴 2 색출
pattern2=re.compile(r"""(\s*□.*)
                    (\s*-.*)\s*
                    (\s*-.*)\s*""",re.VERBOSE)






print(pattern1.search(data).group())

pattern1.findall(data)[1]



data="""1월2일

[전자시황]
□ [스마트폰] 새해 스마트폰 시장에서 ‘폴더블∙5G’가 대세로 자리매김할 전망입니다.
- ‘폴더블폰’ 본격 성장 전망, 올해 폴더블폰 출하량 320만대 예측(카운터포인트리서치), 삼성과 화웨이 후속작 공개와 기타 中 업체 등도 시장 가세
- 독일과 프랑스, 일본 등 주요 국가 잇따라 5G 상용화 실시하며 5G 스마트폰 수요 커질 전망, 5G 스마트폰 시장 규모 작년 1100만대→올해 1억9000만대 전망(IDC)

□ [TV] ‘8K 연합’ 규모가 점차 커지고 있습니다. 
- 8K 산업 생태계 키우기 위해 삼성 주도로 19년 1월 출범함 ‘8K 어소시에이션(8K 협회)’에 글로벌 기업 속속 가세
- 中 디스플레이 업체 차이나스타와 BOE, 대만 반도체 업체 미디어텍 등 신규 가입으로 초기 5개사→현재 22개사로 확대, 8K TV 23년 300만대 돌파 전망(IHS마킷)

□ [TV] 마이크로 LED TV 시장이 주목 받고 있습니다.
- 마이크로LED, 작은 패널 조립해 만든 디스플레이로 성능 뛰어나고 응용 분야 다양해 성장 가능성 高, TV 제조업체들도 앞다퉈 관련 TV 제작 나서
- 中 콩카 최근 마이크로LED TV 개발에 2억1400만달러 투자 확정, 삼성 내년부터 가정용 마이크로LED 라인업 본격 확대, 中∙日 해외 기업들 관련 디스플레이 CES서 전시 

[유통]
□ 유통업체가 올해 생존을 위한 치열한 경쟁을 벌일 전망입니다.
- 최근 소비심리 지표 개선세로 돌아섰지만 내수 부진 등 이어지며 ‘소비 양극화’로 백화점 명품 상품 등 제외하곤 모든 유통 채널 소비 심리 둔화 영향 받을 전망
- 절대 강자 없는 ‘온라인’ 시장 100조원 규모로 포화상태, 공격적 투자 등으로 ‘새판짜기’ 나설 가능성 高, ‘오프라인’ 온라인 중심 사업 확대하고, 매장 체험형 등으로 변신

□ 새해 트렌드로 ‘펀리미엄’이 주목 받고 있습니다.
- 편리함이 곧 프리미엄인 ‘편리미엄’ 시대 도래, 소비자들 시간과 노력 줄여준다면 금액 더 지불하더라도 편리한 상품과 서비스 택할 가능성 高
- 항상 시간 부족한 ‘타임푸어’ 부상하며 ‘편리미엄’ 주목도 高, 가정간편식 시장 편리미엄에 적합한 형태로 진화, 가치 따라 저가와 고가 양면적 소비하는 ‘앰비슈머’도 부상 

□ ‘구독경제’가 생활형으로 진화하고 있습니다. 
- IT기업들 새 사업 모델로 구독경제 점 찍고 관련 시장 진출 박차, 2000년 약 241조원 시장서 15년 470원 규모로 성장, 내년 594조원까지 성장 전망(크레디트스위스)
- 넷마블 웅진코웨이 인수해 구독경제 상품에 IT 운영 노하우 접목하고 스마트홈 진출, ‘요기요’ 정기 할인 구독서비스 ‘슈퍼클럽’ 출시, 쏘카’ 차량 할인 구독 서비스 출시 等

[제품]
□ 애플이 5G 스마트폰을 출시할 예정입니다. 
- 올해 하반기 5G 아이폰 출시 전망, 경쟁사에 비해 다소 늦은 시점이지만 세계 각국에서 5G 상용화 시작되자 본격적인 시장 진출 전망
- 인텔로부터 모뎀칩 사업부 약 1조원에 인수, 전용 5G 모뎀칩 개발 위한 기술력 확보한 상태, LTE로 남아있는 상당수 소비자 아이폰 통해 5G로 넘어갈 확률 高

[CES]
□ 삼성과 LG가 AI냉장고와 8K TV 경쟁을 벌입니다.
- 냉장고 부문서 삼성 ‘패밀리 허브’ 신제품 공개, AI기술로 식재료 구매~식단 관리까지 가능한 스마트한 냉장고, LG ‘인스타뷰 씽큐’ 더 진화한 AI 적용
- TV 부문서 양사 모두 美 소비자기술협회(CTA) 초고화질 인증 획득한 8K TV 전시

[경제시황]
□ 지난해 수출이 10년 만에 두 자릿수 하락했습니다. (산업통상자원부)
- 2019년 수출 총 5424억1000만 달러로 전년대비 10.3% 줄어, 글로벌 금융위기 있었던 09년 -13.9% 이후 10년 만에 두 자릿수로 떨어진 것
- 대외여건 불확실성 증대 및 경기적 요인 복합 작용 때문으로 분석, 실제 美中분쟁 영향(-107억 달러), 반도체 다운사이클(-328억 달러), 유가하락(-134억 달러) 등 추정 

[부동산]
□ 지난달 전국 집값 상승률이 현 정부 들어 최고치를 기록했습니다. (한국감정원)
- 지난해 12월 전국 집값 전월보다 0.38% 오르며 17년 5월 이후 가장 높은 상승률 기록, 이번 통계 조사 기간 지난해 11월12~12월9일로 12.16대책 영향 미반영
- 서울 주택가격 전월 대비 0.86% 오르고 지방 주택가격도 0.16% 오르며 지난해 11월에 이어 2개월 연속 상승, 대전 상승률 1.15%로 전국 17개 시도 가운데 가장 高

1월3일

[전자시황]
□ [스마트폰] 스마트폰 카메라 기능이 디지털카메라 수요를 빠르게 대체하고 있습니다.
- 스마트폰 카메라 성능 10년 전보다 20배 좋아져, SNS로 자신의 일상 공유하는 사람 많아지고, 스마트폰 교체 주기 길어지자 제조사들이 카메라 성능에 집중한 영향
- 디지털 카메라 스마트폰에 밀리는 추세 뚜렷, 디지털 카메라 출하량 10년 1억2146만대로 정점 찍은 후 18년 1942만대까지 축소(스태티스타)

□ [주방가전] 주방가전 업체들이 ‘프리미엄’을 강화합니다.
- 구매력 있는 소비자들 겨냥해 프리미엄 제품 선보이는 중견 주방가전 업체들 多, 단일 상품으로 인기 얻는 현상에서 벗어나 ‘멀티 히트 원더’로 도약 꾀하는 모습
- 휴롬 원액기 아성 무너뜨릴 찌는 방식 멀티쿠커 ‘휴롬스팀’ 출시, 쿠쿠 50~60만원대 프리미엄 밥솥 출시, 쿠첸 요리 편의성 높인 150만원대 로봇쿠커 출시 等

[유통]
□ 온라인 음식 매출이 1조원을 돌파했습니다. (통계청)
- ‘2019년 11월 온라인쇼핑 동향’ 결과 전체 거래액 12조7576억원으로 전년 동월 대비 20.2% 증가, 월간 거래액 12조원 넘어선 건 통계 이래 처음
- 온라인 음식 매출 증가세 눈에 띄어, 전화 통한 배달 제외하고 스마트폰 앱이나 PC 등 통한 음식서비스업 매출 1년 전보다 100.3% 증가한 1조242억원 집계 

□ 편의점 업계도 ‘배달 서비스’ 강화에 나섭니다.
- CU, 요기요 등 배달앱과 협업해 배달 경쟁 강화 나서, 지난해 7월 2000점이었던 배달 가능 점포 수 약 5개월 만인 올해 1월 초 3000점까지 확대
- 현재 배달서비스 운영 희망 등록대기 점포만 약 2000점 달해 올해 1분기 내 5000점까지 확대 전망

□ 온라인 유통업체들의 경쟁이 치열합니다. 
- 쿠팡 지난해 12조원 거래액 돌파하며 성장세 1위 기록, 재무건전성에 대한 우려 안고 10만평 규모 물류센터 조성하는 등 새해에도 배송 서비스 강화
- 이베이 멤버십 혜택 확대 통해 업계에서 유일하게 ‘흑자’ 경영 중, 네이버쇼핑 ‘검색엔진’이란 강점으로 지난해 9조원 이상 거래액 기록하며 업계 3위 도약설 等

[제품]
□ LG가 플래그십 스마트폰 ‘LG V60 씽큐’를 이르면 오는 3월 출시합니다. 
- V50∙V50S 씽큐에 이은 3번째 듀얼스크린폰, 다음달 MWC 2020에서 공개한 뒤 이르면 3월 늦어도 4월께 이동통신 3사 통해 국내 출시 예정
- 제품 장착에 따른 두께와 무게, 디스플레이 베젤, 노치 등 여러 부분에서 V50보다 발전된 형태 보일 것으로 전망, 삼성 차기 폴더블폰과 갤럭시S11 등과 경쟁 예상 

[신성장품목]
□ 애플이 ‘가상 오디오’ 기술 특허를 취득했습니다. 
- 애플 노트북 스피커 여러 개 있는 듯한 착각 불러일으키는 ‘가상 오디오’ 기술 특허 취득, 노트북 사용자의 사운드 몰입감 훨씬 높여줄 수 있을 것이란 기대감 有
- 특허 핵심 ‘크로스토크 캔슬링’으로 좌우 스테레오 사운드 섞이는 ‘크로스토크’ 현상 막아 소리 입체적으로 전달

□ 교원웰스가 신개념 식물 재배기를 선보였습니다. 
- 교원 생활가전 브랜드 ‘웰스’가 자사 식물 재배기 ‘웰스팜’에 교육 프로그램 접목한 ‘키즈팜’ 출시, 식물 관찰과 수학 체험으로 자연 탐구 활동 가능한 신개념 식물 재배기
- 아이들이 재배기에 직접 씨앗 심고 식물 자라는 과정 관찰, 탐구하며 관찰일기 쓰거나 제공되는 프로그램 통해 채소 자라나는 모습 애니메이션 형태로 관찰 가능 

[CES]
□ 올해 행사는 글로벌 기업들간 AI전쟁터가 될 것이란 전망입니다.
- 삼성, LG, 인텔 등 모든 기업들 ‘AI’ 핵심 제품(서비스)으로 내세운 채 행사 참석, CES 주관 CTA도 ‘CES 2020’을 ‘AI 전시회’로 공인, 참가 전문가들도 AI 분야 인재 가장 多
- 기술 개발 넘어 실제 생활 적용 가능한 아이디어 쏟아질 것으로 예측, 국내 대기업들 ‘생활형 AI’ 주제로 전시, 완성차 업체들 ‘자율주행차’ 등 미래車 공개 等

□ 국내 디스플레이 업계가 CES 2020에 총출동합니다.
- LGD, OLED 기술력 확장성 주제로 공간 특성과 소비자 라이프스타일 맞춘 디스플레이 공개, 65인치 UHD 롤다운 OLED TV, 48인치 OLED TV 등 세계 최초 공개 
- 삼성D, QD디스플레이 홍보 위해 라스베이거스 시내 앙코르 호텔에 고객사 대상으로 비공개 부스 꾸릴 예정, 다양한 라인업의 시제품 등 공개 

"""
