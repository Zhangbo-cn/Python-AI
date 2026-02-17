import streamlit as st

st.title = '聊天机器人案例'

st.write('这是一个段落标签内容')
st.write('这是一个段落标签内容')
st.write('这是一个段落标签内容')

st.write('# 一级标题')
st.write('## 二级标题')
st.write('### 三级标题')

st.image('data/a.png', width=300)

st.divider()

st.table(data={
    'name': ['张三', '李四'],
    'age': [27, 29],
    'city': ['北京', '上海']
})

name = st.text_input('请输入您的名字：')
if name:
    st.write(name)


password = st.text_input('密码是多少？', type='password')

st.number_input('请输入您的年龄：', value=20, min_value=10, max_value=30, step=1)

st.text_area('请输入多行内容：')

prompt = st.chat_input('请输入您的问题：')
if prompt:
    st.write(f'用户输入的问题：{prompt}')
