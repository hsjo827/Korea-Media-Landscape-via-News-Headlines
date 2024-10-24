import re
# 필요한 폰트 경로 설정
font_path = 'C:\\Users\\user\\anaconda3\\envs\\text\\Lib\\site-packages\\matplotlib\\mpl-data\\fonts\\malgun.ttf'

# 신문사 분류
보수 = ['조선일보', '중앙일보', '동아일보']
진보 = ['오마이뉴스', '경향신문', '한겨레']
기타 = ['연합뉴스', '매일경제', '머니투데이']
# 언론사 명 리스트
other_media = ['SBS Biz','한국경제TV','뉴스1','JTBC','채널A','MBN','SBS','MBC','YTN','뉴시스',
                'KBS','TV조선','연합뉴스TV','매경이코노미','한경비즈니스','월간산','한겨레21',
                '이코노미스트','더스쿠프','주간경향','신동아','시사저널','주간조선','시사IN',
                '주간동아','농민신문','기자협회보','코메디닷컴','코리아헤럴드','코리아중앙데일리',
                '일다','뉴스타파','동아사이언스','헬스조선','여성신문','서울신문','문화일보','세계일보',
                '한국일보','국민일보','아이뉴스24','디지털데일리','데일리안','머니S','블로터','더팩트',
                '프레시안','지디넷코리아','미디어오늘','디지털타임스','노컷뉴스','전자신문','서울경제',
                '헤럴드경제','비즈워치','아시아경제','파이낸셜뉴스','조선비즈','이데일리','조세일보','한국경제']

all_media = 진보 + 보수 + 기타 + other_media # 언론사 리스트 모두 합치기

pattern = r'(?<=es_).*(?=\.)' # csv 파일명에서 키워드만 추출하는 정규표현식
