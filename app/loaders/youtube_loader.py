from langchain_community.document_loaders import YoutubeLoader


def load_youtube(url: str):
    try:
        loader = YoutubeLoader.from_youtube_url(
        url,
        language=["hi", "en"],
        add_video_info=False,
    )

        return loader.load()

    except Exception as e:
        print(type(e))
        raise