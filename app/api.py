from locust import TaskSet, task, HttpUser
from common.auth import login, pick_user
from common.config import fake


class ApiRequests(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        login(self.client)
        pass

    def on_stop(self):
        pass

    @task(1)
    def activity_points(self):
        self.client.get('/api/v1/activitypoint/statistic/1')
        self.client.get('/api/v1/activitypoint/package')
        self.client.get('/api/v1/activitypoint/setting')
        self.client.get('/api/v1/activitypoint/transaction?page=1')
        self.client.get('/api/v1/activitypoint/package-transaction?page=1')
        pass

    @task(1)
    def activity_points(self):
        self.client.get('/api/v1/activitypoint/statistic/1')
        self.client.get('/api/v1/activitypoint/package')
        self.client.get('/api/v1/activitypoint/setting')
        self.client.get('/api/v1/activitypoint/transaction?page=1')
        self.client.get('/api/v1/activitypoint/package-transaction?page=1')
        pass

    def app_blogs(self):
        self.client.get('/api/v1/blog?view=pending&page=1')
        self.client.get('/api/v1/blog?view=draft&page=1')
        self.client.get('/api/v1/blog?view=my_pending&page=1')
        self.client.get('/api/v1/blog?view=my&page=1')
        self.client.get('/api/v1/blog?page=1')
        self.client.get('/api/v1/blog?view=feature')
        self.client.get('/api/v1/blog-category')
        self.client.get('/api/v1/blog?sort=most_viewed&page=1&limit=10')
        self.client.get('/api/v1/blog?view=friend&page=1')
        self.client.get('/api/v1/blog?category_id=1&view=search&page=1')
        self.client.get('/api/v1/core/form/blog.store')
        self.client.post('/api/v1/blog', None, {
            'title': fake.sentence(nb_words=5),
            'text': fake.text(max_nb_chars=200),
            "module_id": "blog",
            "privacy": 0,
            "draft": 0,
            "tags": ["aspernatur"],
            "owner_id": 0,
            "attachments": [],
            "categories": [1],
        })
        pass

    @task(1)
    def app_events(self):
        self.client.get('/api/v1/event-category')
        self.client.get('/api/v1/event?sort=most_interested')
        self.client.get('/api/v1/event?sort=recent&view=interested&page=1')
        self.client.get('/api/v1/event?sort=recent&view=going&page=1')
        self.client.get('/api/v1/event?limit=6&view=feature')
        self.client.get('/api/v1/event?sort=recent&view=going&page=1')
        self.client.get('/api/v1/event?sort=recent&view=interested&page=1')
        self.client.get('/api/v1/event?page=1')
        self.client.get('/api/v1/event?view=my&page=1')
        self.client.get('/api/v1/event?view=my_pending&page=1')
        self.client.get('/api/v1/event?user_id=1&when=upcoming&page=1')
        self.client.get('/api/v1/event?view=friend&page=1')
        self.client.get('/api/v1/event?sort=end_time&view=related&when=past&page=1')
        self.client.get('/api/v1/event?view=invites&page=1')
        self.client.get('/api/v1/event?category_id=1&view=search&page=1')
        self.client.get('/api/v1/event?view=pending&page=1')

        self.client.get('/api/v1/event/form')
        self.client.post('/api/v1/event', None, {
            "module_id": "event",
            "privacy": 0,
            "is_online": 0,
            "owner_id": 0,
            "attachments": [],
            "start_time": "2023-02-14T06:58:49.200347Z",
            "end_time": "2023-02-15T07:58:00.000Z",
            "location": {
                "address": "Hồ Chí Minh, Thành phố Hồ Chí Minh, Việt Nam",
                "lat": 10.8230989,
                "lng": 106.6296638,
                "short_name": "VN"
            },
            "categories": [1],
            "name": fake.sentence(nb_words=5),
            "text": fake.text(max_nb_chars=200)
        })

        pass

    @task(1)
    def app_feed(self):
        self.client.get('/api/v1/feed/check-new?last_feed_id=1')
        self.client.get('/api/v1/feed?view=latest&page=1')
        pass

    @task(1)
    def post_bg_status(self):
        self.client.post('/api/v1/feed', None, {
            "user_status": fake.text(max_nb_chars=200),
            "post_type": "activity_post",
            "privacy": 0, "status_background_id": 1
        })
        pass

    @task(1)
    def post_checkin(self):
        self.client.post('/api/v1/feed', None, {
            "user_status": fake.text(max_nb_chars=200),
            "post_type": "activity_post",
            "location": {"address": "Sân vận động quốc gia Singapore", "lat": 1.304013, "lng": 103.8748426},
            "privacy": 0})
        pass

    @task(1)
    def create_poll(self):
        self.client.post('/api/v1/feed', None, {
            "user_status": fake.text(max_nb_chars=200),
            "post_type": "poll",
            "tagged_friends": [],
            "privacy": 0,
            "poll_multiple": 0,
            "enable_close": 0,
            "poll_public": 1,
            "poll_answers": [
                {"answer": fake.sentence(nb_words=5), "order": 1},
                {"answer": fake.sentence(nb_words=5), "order": 2}],
            "poll_question": fake.sentence(nb_words=5),
            "poll_attachments": []})
        pass

    @task(1)
    def app_friends(self):
        self.client.get('/api/v1/friend/list?page=1')
        self.client.get('/api/v1/friend?page=1')
        self.client.get('/api/v1/friend/request?view=pending&page=1')
        self.client.get('/api/v1/friend/request?view=send&page=1')
        self.client.get('/api/v1/core/form/core.privacy_option.store')
        self.client.get('/api/v1/friend/request?view=pending&limit=10&page=1')
        pass

    @task(1)
    def create_friend_list(self):
        self.client.post('/api/v1/core/custom-privacy-option', None, {
            'name': fake.sentence(nb_words=3)
        })
        pass

    @task(1)
    def app_groups(self):
        self.client.get('/api/v1/group/category')
        self.client.get('/api/v1/group?limit=6&view=feature')
        self.client.get('/api/v1/group?sort=most_member&page=1&limit=10')
        self.client.get('/api/v1/group?page=1')
        self.client.get('/api/v1/group?view=my&page=1')
        self.client.get('/api/v1/group?view=my_pending&page=1')
        self.client.get('/api/v1/group?view=friend&page=1')
        self.client.get('/api/v1/group?view=joined&page=1')
        self.client.get('/api/v1/group?view=invited&page=1')
        self.client.get('/api/v1/group?view=pending&page=1')
        self.client.get('/api/v1/friend?limit=10')
        self.client.get('/api/v1/group/form')
        self.client.get('/api/v1/group?category_id=10&view=search&page=1')
        self.client.get('/api/v1/group?q=Knowledge&category_id=10&view=search')
        self.client.get('/api/v1/group?q=Knowledge&when=this_month&category_id=10&view=search')
        pass

    @task(1)
    def create_group(self):
        self.client.post('/api/v1/group', None, {
            'category_id': 10,
            'name': fake.sentence(nb_words=5),
            'reg_method': 0,
            'text': fake.text(max_nb_chars=200)
        })
        pass

    @task(1)
    def bg_collections(self):
        self.client.get('/api/v1/pstatusbg-collection')
        pass

    @task(1)
    def notifications(self):
        self.client.get('/api/v1/notification?limit=10&page=1')
        self.client.get('/api/v1/notification?page=1')

    @task(1)
    def mark_all_as_read(self):
        self.client.post('/api/v1/notification/markAllAsRead')
        pass

    @task(1)
    def announcements(self):
        self.client.get('/api/v1/announcement')
        pass

    @task(1)
    def feeds(self):
        self.client.get('/api/v1/feed?view=latest&last_feed_id=54&page=1')
        pass

    @task(1)
    def next_feeds(self):
        self.client.get('/api/v1/feed?view=latest&last_feed_id=100&page=2')
        pass

    @task(1)
    def status(self):
        self.client.get('/api/v1/core/status')
        pass

    @task(1)
    def shortcut(self):
        self.client.get('/api/v1/user/shortcut')
        pass

    @task(1)
    def edit_shortcut(self):
        self.client.get('/api/v1/user/shortcut/edit?page=1')
        pass

    @task(1)
    def app_marketplace(self):
        self.client.get('/api/v1/marketplace-category')
        self.client.get('/api/v1/marketplace?view=feature')
        self.client.get('/api/v1/marketplace?sort=most_viewed&page=1&limit=10')
        self.client.get('/api/v1/marketplace?view=all&page=1')
        self.client.get('/api/v1/marketplace?view=my&page=1')
        self.client.get('/api/v1/marketplace?view=my_pending&page=1')
        self.client.get('/api/v1/marketplace?view=invite&page=1')
        self.client.get('/api/v1/marketplace?view=history&page=1')
        self.client.get('/api/v1/marketplace?view=expired&page=1')
        self.client.get('/api/v1/marketplace?view=friend&page=1')
        self.client.get('/api/v1/marketplace?view=pending&page=1')
        self.client.get('/api/v1/marketplace-invoice')
        self.client.get('/api/v1/marketplace?category_id=1&view=search&page=1')
        self.client.get('/api/v1/core/form/marketplace.store')

        pass

    @task(1)
    def create_marketplace(self):
        self.client.post('/api/v1/marketplace', None, {
            "privacy": 0,
            "owner_id": 1,
            "attachments": [],
            "location": {
                "address": "Hồ Chí Minh, Thành phố Hồ Chí Minh, Việt Nam",
                "lat": 10.8230989,
                "lng": 106.6296638,
                "short_name": "VN"
            },
            "allow_payment": 0,
            "allow_point_payment": 0,
            "is_sold": 0,
            "auto_sold": 1,
            "categories": [1],
            "is_moderator": 0,
            "attached_photos": [],
            "title": fake.text(max_nb_chars=200),
            "short_description": "def",
            "text": fake.text(max_nb_chars=200),
            "price_USD": "111",
            "price_EUR": "22",
            "price_GBP": "33"})

        pass

    @task(1)
    def app_pages(self):
        self.client.get('/api/v1/page?sort=most_member&page=1&limit=10')
        self.client.get('/api/v1/page/category')
        self.client.get('/api/v1/page?limit=6&view=feature')

        self.client.get('/api/v1/page?view=pending&page=1')
        self.client.get('/api/v1/page?view=my_pending&page=1')
        self.client.get('/api/v1/page?view=my&page=1')
        self.client.get('/api/v1/page?page=1')

        self.client.get('/api/v1/page?view=invited&page=1')
        self.client.get('/api/v1/page?view=liked&page=1')
        self.client.get('/api/v1/page?view=friend&page=1')
        self.client.get('/api/v1/page?category_id=10&view=search&page=1')
        self.client.get('/api/v1/page?q=Knowledge&category_id=10&view=search')
        self.client.get('/api/v1/page?q=Knowledge&when=this_month&category_id=10&view=search')
        self.client.get('/api/v1/page/form')
        self.client.get('/api/v1/friend?limit=10')
        pass

    @task(1)
    def create_page(self):
        self.client.post('/api/v1/page', None, {
            'category_id': 10,
            'name': fake.sentence(nb_words=5),
            'text': fake.text(max_nb_chars=200)
        })
        pass

    @task(1)
    def app_photos(self):
        self.client.get('/api/v1/photo?limit=6&view=feature')
        self.client.get('/api/v1/photo-category')

        self.client.get('/api/v1/photo?view=pending&page=1')
        self.client.get('/api/v1/photo-album?view=my&page=2')
        self.client.get('/api/v1/photo-album?page=1')
        self.client.get('/api/v1/photo?view=friend&page=1')
        self.client.get('/api/v1/photo?category_id=1&view=search&page=1')
        self.client.get('/api/v1/photo?view=my_pending&page=1')
        self.client.get('/api/v1/photo?view=my&page=1')
        self.client.get('/api/v1/photo?page=1')
        self.client.get('/api/v1/photo?sort=most_liked&page=1&limit=10')
        self.client.get('/api/v1/photo-album?limit=6&view=feature')
        self.client.get('/api/v1/core/form/photo.upload')
        self.client.get('/api/v1/core/form/photo_album.store')
        pass

    @task(1)
    def upload_photo(self):
        # todo TBD
        pass

    @task(1)
    def create_album(self):
        # todo TBD
        pass

    @task(1)
    def app_poll(self):
        self.client.get('/api/v1/poll?view=search&page=1')
        self.client.get('/api/v1/poll?view=friend&page=1')
        self.client.get('/api/v1/poll?view=my&page=1')
        self.client.get('/api/v1/poll?page=1')
        self.client.get('/api/v1/poll?view=feature')
        self.client.get('/api/v1/poll?sort=most_viewed&page=1&limit=10')
        self.client.get('/api/v1/poll?view=my_pending&page=1')
        self.client.get('/api/v1/poll?view=pending&page=1')
        self.client.get('/api/v1/core/form/poll.store')
        pass

    @task(1)
    def create_poll(self):
        self.client.post('/api/v1/poll', None, {
            "is_multiple": 0,
            "enable_close": 0,
            "public_vote": 1,
            "privacy": 0,
            "answers":
                [{"answer": "ded", "order": 1},
                 {"answer": "ddd", "order": 2}],
            "owner_id": 0, "attachments": [],
            "has_banner": 0,
            "question": "abcd",
            "text": "<p>addd</p>",
            "submit": 1})
        pass

    @task(1)
    def app_quiz(self):
        self.client.get('/api/v1/quiz?view=search&page=1')
        self.client.get('/api/v1/quiz?view=pending&page=1')
        self.client.get('/api/v1/quiz?view=friend&page=1')
        self.client.get('/api/v1/quiz?view=my_pending&page=1')
        self.client.get('/api/v1/quiz?view=my&page=1')
        self.client.get('/api/v1/quiz?page=1')
        self.client.get('/api/v1/quiz?view=feature')
        self.client.get('/api/v1/quiz?sort=most_played&page=1&limit=10')
        self.client.get('/api/v1/quiz/form')
        pass

    @task(1)
    def create_quiz(self):
        self.client.post('/api/v1/quiz', None, {
            "questions": [{
                "question": fake.sentence(nb_words=5),
                "ordering": 1,
                "answers": [
                    {"answer": fake.sentence(nb_words=5), "is_correct": 1, "ordering": 1},
                    {"answer": fake.sentence(nb_words=5), "is_correct": 0, "ordering": 2},
                    {"answer": fake.sentence(nb_words=5), "is_correct": 0, "ordering": 3},
                    {"answer": fake.sentence(nb_words=5), "is_correct": 0, "ordering": 4}]}
            ],
            "title": fake.sentence(nb_words=5),
            "text": fake.text(max_nb_chars=200),
            "attachments": [],
            "privacy": 0,
            "owner_id": 0})

        pass

    @task(1)
    def saved_items(self):
        self.client.get('/api/v1/saveditems?page=1')
        self.client.get('/api/v1/saveditems-collection?page=1')
        self.client.get('/api/v1/saveditems?open=all&type=blog&page=1')
        self.client.get('/api/v1/saveditems-collection/form')
        pass

    @task(1)
    def create_collection(self):
        self.client.post('/api/v1/saveditems-collection', None, {
            'name': fake.sentence(nb_words=5)
        })
        pass

    @task(1)
    def app_user_settings(self):
        self.client.get('/api/v1/account/setting')
        self.client.get('/api/v1/account/notification?channel=database')
        self.client.get('/api/v1/account/notification?channel=mail')
        self.client.get('/api/v1/account/profile-privacy/1')
        self.client.get('/api/v1/user/account/review-form')
        self.client.get('/api/v1/mfa/service')
        self.client.get('/api/v1/account/item-privacy/1')
        self.client.get('/api/v1/account/blocked-user')
        self.client.get('/api/v1/feed?is_preview_tag=1&page=1')
        self.client.get('/api/v1/account/invisible')
        self.client.get('/api/v1/payment-gateway/configuration')
        self.client.get('/api/v1/account/profile-menu/1')
        self.client.get('/api/v1/user/account/name-form')
        self.client.get('/api/v1/user/account/email-form')
        self.client.get('/api/v1/user/account/username-form')
        self.client.get('/api/v1/user/account/password-form')
        self.client.get('/api/v1/user/account/timezone-form')
        self.client.get('/api/v1/user/account/currency-form')
        pass

    @task(1)
    def app_browse_users(self):
        self.client.get('/api/v1/user?page=1')
        self.client.get('/api/v1/user?view=recommend&page=1')
        self.client.get('/api/v1/user?view=recent&page=1')
        self.client.get('/api/v1/user?view=featured&page=1')
        self.client.get('/api/v1/user/profile/form')
        pass

    @task(1)
    def view_user(self):
        user_id = pick_user()[0]
        self.client.get('/api/v1/user/' + user_id)
        self.client.get('/api/v1/feed?user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/photo?sort=latest&user_id=' + user_id)
        self.client.get('/api/v1/friend?limit=6&user_id=' + user_id + '&view=profile')
        self.client.get('/api/v1/friend?limit=12&sort=latest&user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/user/info/' + user_id)
        self.client.get('/api/v1/friend/request?user_id=' + user_id + '&view=pending&page=1')
        self.client.get('/api/v1/photo?sort=recent&user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/photo-album?sort=latest&user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/video?limit=12&sort=recent&user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/page?limit=12&sort=latest&user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/marketplace?user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/blog?user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/poll?user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/quiz?user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/video?user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/event?user_id=' + user_id + '&page=1')
        self.client.get('/api/v1/forum-thread?user_id=' + user_id + '&page=1')
        pass

    @task(1)
    def browse_videos(self):
        self.client.get('/api/v1/video/category')
        self.client.get('/api/v1/video?view=feature')
        self.client.get('/api/v1/video?sort=most_viewed&page=1&limit=10')
        self.client.get('/api/v1/video?page=1')
        self.client.get('/api/v1/video?view=my&page=1')
        self.client.get('/api/v1/video?view=my_pending&page=1')
        self.client.get('/api/v1/video?view=friend&page=1')
        self.client.get('/api/v1/video?view=pending&page=1')
        self.client.get('/api/v1/video?category_id=1&view=search&page=1')
        self.client.get('/api/v1/core/form/video.store')
        self.client.get('/api/v1/core/form/video.share')
        pass

    @task(1)
    def upload_video(self):
        # todo TBD
        pass

    @task(1)
    def share_video(self):
        # todo TBD
        pass
