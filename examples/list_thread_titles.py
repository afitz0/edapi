from edapi import EdAPI


def main():
    ed = EdAPI()
    ed.login()

    threads = ed.list_all_threads(67447)
    for thread in threads:
        print(f"#{thread['number']} ({thread['id']}) {thread['title']}")


if __name__ == "__main__":
    main()
