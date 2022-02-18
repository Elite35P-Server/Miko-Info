import streamlit as st
import requests


st.title('Miko Info')
base_url = 'https://api.nyahello.jp/v2'

res1 = requests.get(f'{base_url}/youtube')

if res1.status_code != 200:
    e = RuntimeError(f'status: {res1.status_code}, response: {res1.text}')
    st.exception(e)
    
def youtube_videos(order: str = 'created_at', skip: int = 0, limit: int = 5):
    params = {
        'order': order,
        'skip': skip,
        'limit': limit,
    }
    res = requests.get(f'{base_url}/youtube/videos/', params=params)
    if res.status_code != 200:
        e = RuntimeError(f'status: {res.status_code}, response: {res.text}')
        st.exception(e)
    return res.json()

ch_data = res1.json()

st.markdown('## YouTube')
st.markdown('***')

st.markdown('### Channel Name')
st.write(ch_data['name'])

st.markdown('### Channel Description')
st.write(ch_data['description'])

st.markdown('### Channel Icon')
st.image(ch_data['icon'])

st.markdown('### Channel Subscriber Count')
st.write(ch_data['subsc_count'])

st.markdown('### Channel Video Count')
st.write(ch_data['video_count'])

st.markdown('### Channel Play Count')
st.write(ch_data['play_count'])

st.markdown('### Channel Status')
if ch_data['status'] == 'live':
    video = youtube_videos(order='live', limit=1)[0]
    st.markdown('#### Status')
    st.markdown('***Live***')
    st.markdown('#### Live Detail')
    st.write(video['title'])
    st.video(video['url'])
    st.write(video['description'])
    
elif ch_data['status'] == 'upcoming':
    video = youtube_videos(order='upcoming', limit=1)[0]
    st.markdown('#### Status')
    st.markdown('***Upcoming***')
    st.markdown('#### Upcoming Detail')
    st.write(video['title'])
    st.video(video['url'])
    st.write(video['description'])
    
elif ch_data['status'] == 'none':
    video = youtube_videos(order='created_at', limit=1)[0]
    st.markdown('#### Status')
    st.markdown('***None***')
    st.markdown('#### Latest Video Detail')
    st.write(video['title'])
    st.video(video['url'])
    st.write(video['description'])