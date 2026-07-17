from app.postprocessing.mmr import text_similarity


def main():
    print("Testing text similarity...\n")

    score = text_similarity(
        "TCP is reliable",
        "TCP is reliable and ordered"
    )
    print(f"Test 1: {score:.4f}")

    score = text_similarity(
        "TCP Handshake",
        "Flow Control"
    )
    print(f"Test 2: {score:.4f}")

    score = text_similarity(
        "TCP",
        "TCP"
    )
    print(f"Test 3: {score:.4f}")


if __name__ == "__main__":
    main()