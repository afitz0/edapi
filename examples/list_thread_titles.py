from edapi import EdAPI

COURSE_ID = 0  # TODO: replace with your course id


def main():
    ed = EdAPI()
    ed.login()

    threads = ed.list_all_threads(COURSE_ID)
    for thread in threads:
        print(f"#{thread['number']} ({thread['id']}) {thread['title']}")


if __name__ == "__main__":
    main()
