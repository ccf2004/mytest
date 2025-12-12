import streamlit as st

#修改标签页的文字和图标
st.set_page_config(page_title='相册', page_icon='🐒')

st.title("我的相册")
# 初始化图片索引ind，默认显示第0张图片
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

images = [
    {
        'url':"https://ts4.tc.mm.bing.net/th/id/OIP-C.F15Td8baE_F5y4UzxGppDwHaE7?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
        'text':'猫'
    },{
         'url':"https://img.pconline.com.cn/images/upload/upc/tx/itbbs/1406/16/c18/35339323_1402908540795.jpg",
         'text':'猴子'
    },{
         'url':"https://ts1.tc.mm.bing.net/th/id/OIP-C._ITStaPCyDNy4feFPGQxWgHaFG?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
         'text':'兔子'
    }]
            
# st.image()总共两个参数，url：图片地址 caption:图片的备注
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])

# 下一张
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)
# 上一张
def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(images)

c1,c2=st.columns(2)

with c1:
    st.button("下一张",on_click=nextImg,use_container_width=True)

with c2:
    st.button("上一张",on_click=lastImg,use_container_width=True)
