#!/usr/bin/env python3
"""Generate bilingual (EN/VI) privacy policy pages for each Takaction app.

Run from anywhere:  python3 tools/build-policies.py
Output: privacy/<slug>/index.html  (+ privacy/policy.css)

Edit CONFIG / APPS below, then re-run. Do not hand-edit the generated files.
Every claim below was checked against each app's source on 2026-11-14.
"""
import html
import pathlib

# ---------------------------------------------------------------- CONFIG
CONTACT_EMAIL = "takcationsupport@gmail.com"
LAST_UPDATED = "2026-11-14"
DEVELOPER = "Takaction"
PLAY_DEV = "https://play.google.com/store/apps/dev?id=4733093585231168003"
# ---------------------------------------------------------------------

ROOT = pathlib.Path(__file__).resolve().parent.parent
PL = "https://play-lh.googleusercontent.com/%s=s128"

SECTION_KEYS = ["collect", "local", "perms", "services", "children"]

APPS = {
    # ------------------------------------------------------------------ CubeSnap
    "cubesnap": {
        "name": "CubeSnap: Rubik Solver 3D",
        "icon": PL % "lTiqbnicWCLmoQe8ysFGA5iKYje95dNi24FUyRQKBpumkAUPPanMRlsP-Hi38fJR5f1R8d-HChP2eJJidkR9i5g",
        "en": {
            "collect": [
                "<b>Camera images.</b> Used only while you scan your cube. Colors are read on your device; we do not upload or store the images.",
                "<b>Advertising data (Google AdMob).</b> When ads are shown, Google may collect your IP address, advertising ID, device and app identifiers, ad interactions and diagnostics.",
                "<b>Usage analytics (Firebase Analytics).</b> Off by default. It is turned on only when the consent state allows it; in the EEA, the UK and other regions that require consent, only after you agree.",
                "<b>Purchase information.</b> Purchases are handled by Google Play. We never see your payment details; the app receives a purchase token to unlock what you bought and to restore it later.",
                "<b>No account.</b> We do not ask for your name, email or phone number.",
            ],
            "local": ["Settings, lesson progress, your daily free-solve count, ad-reward counters, and your unlock status and solve credits."],
            "perms": [
                "<b>Camera</b> — to scan the cube. You can revoke it any time in Android settings.",
                "<b>Internet and network state</b> — to load ads and process purchases.",
                "<b>Advertising ID</b> — used by Google’s ad library.",
            ],
            "services": [
                "<b>Ads.</b> CubeSnap includes 1 free solve per day. You can watch a rewarded ad to earn extra solves (limited per day), and a banner appears on the Home screen. Ads are served by Google AdMob. Where required, a consent form (Google User Messaging Platform) appears first, and you can change your choice later in Settings. Unlocking the app removes ads.",
                "<b>Purchases.</b> Through Google Play Billing you can buy a one-time unlock or solve packs.",
            ],
            "children": "CubeSnap is a general-audience app and is not directed to children under 13.",
        },
        "vi": {
            "collect": [
                "<b>Hình ảnh từ camera.</b> Chỉ dùng khi bạn quét khối Rubik. Màu được đọc ngay trên thiết bị; chúng tôi không tải lên hay lưu ảnh.",
                "<b>Dữ liệu quảng cáo (Google AdMob).</b> Khi hiển thị quảng cáo, Google có thể thu thập địa chỉ IP, mã quảng cáo, mã định danh thiết bị và ứng dụng, tương tác với quảng cáo và thông tin chẩn đoán.",
                "<b>Phân tích sử dụng (Firebase Analytics).</b> Mặc định tắt. Chỉ bật khi trạng thái đồng ý cho phép; ở EEA, Vương quốc Anh và các vùng yêu cầu đồng ý thì chỉ sau khi bạn đồng ý.",
                "<b>Thông tin giao dịch.</b> Giao dịch do Google Play xử lý. Chúng tôi không thấy thông tin thanh toán; ứng dụng nhận mã giao dịch để mở khóa phần bạn đã mua và khôi phục sau này.",
                "<b>Không cần tài khoản.</b> Chúng tôi không hỏi họ tên, email hay số điện thoại.",
            ],
            "local": ["Cài đặt, tiến độ bài học, số lượt giải miễn phí trong ngày, bộ đếm phần thưởng quảng cáo, trạng thái mở khóa và số lượt giải đã mua."],
            "perms": [
                "<b>Camera</b> — để quét khối Rubik. Bạn có thể thu hồi quyền bất kỳ lúc nào trong cài đặt Android.",
                "<b>Internet và trạng thái mạng</b> — để tải quảng cáo và xử lý giao dịch.",
                "<b>Mã quảng cáo (Advertising ID)</b> — do thư viện quảng cáo của Google sử dụng.",
            ],
            "services": [
                "<b>Quảng cáo.</b> CubeSnap cho 1 lượt giải miễn phí mỗi ngày. Bạn có thể xem quảng cáo có thưởng để nhận thêm lượt (có giới hạn mỗi ngày), và có banner ở màn hình Home. Quảng cáo do Google AdMob phân phối. Ở nơi pháp luật yêu cầu, biểu mẫu đồng ý (Google User Messaging Platform) hiện trước, và bạn có thể đổi lựa chọn sau trong Cài đặt. Mở khóa ứng dụng sẽ bỏ quảng cáo.",
                "<b>Giao dịch mua.</b> Qua Google Play Billing, bạn có thể mua mở khóa một lần hoặc các gói lượt giải.",
            ],
            "children": "CubeSnap là ứng dụng cho mọi đối tượng và không nhắm tới trẻ em dưới 13 tuổi.",
        },
    },
    # ------------------------------------------------------------------ Number Garden
    "number-garden": {
        "name": "Number Garden: Math for Kids",
        "icon": PL % "efFogaojQLZTU2l4gcl7fK_J6Oy2XItsgWCTWgjhVXs4RflQm3CX4ubGd8LuAC4BnmoQbB7SofJMRZ0SnJJd",
        "en": {
            "collect": [
                "<b>No personal information.</b> The app has no accounts, no chat and no social features. We do not ask for or collect a child’s name, email, location or photos.",
                "<b>No ads and no analytics.</b> The app contains no advertising or analytics libraries.",
            ],
            "local": ["Learning progress (answers, completed puzzles, quiz results) and settings, so your child can pick up where they left off."],
            "perms": ["The app requests no sensitive permissions. It only adjusts audio settings so sounds can play."],
            "services": ["Number Garden contains no advertising and no in-app purchases."],
            "children": "Number Garden is designed for children aged 5 and up. We do not knowingly collect personal information from children. "
                        "The Parent corner, including the “Show what you know” quiz, is intended for adults and its results stay on the device. "
                        "If you believe a child has given us personal information, contact us and we will delete it.",
        },
        "vi": {
            "collect": [
                "<b>Không thu thập thông tin cá nhân.</b> Ứng dụng không có tài khoản, trò chuyện hay tính năng mạng xã hội. Chúng tôi không hỏi hay thu thập tên, email, vị trí hoặc ảnh của trẻ.",
                "<b>Không quảng cáo, không phân tích.</b> Ứng dụng không chứa thư viện quảng cáo hay phân tích nào.",
            ],
            "local": ["Tiến độ học (câu trả lời, câu đố đã hoàn thành, kết quả quiz) và cài đặt, để bé tiếp tục từ chỗ đang học."],
            "perms": ["Ứng dụng không yêu cầu quyền nhạy cảm nào. Nó chỉ điều chỉnh cài đặt âm thanh để phát tiếng."],
            "services": ["Number Garden không có quảng cáo và không có giao dịch mua trong ứng dụng."],
            "children": "Number Garden được thiết kế cho trẻ từ 5 tuổi. Chúng tôi không cố ý thu thập thông tin cá nhân của trẻ em. "
                        "Góc phụ huynh, gồm bài quiz “Show what you know”, dành cho người lớn và kết quả chỉ nằm trên thiết bị. "
                        "Nếu bạn cho rằng trẻ đã cung cấp thông tin cá nhân cho chúng tôi, hãy liên hệ để chúng tôi xóa.",
        },
    },
    # ------------------------------------------------------------------ Krog
    "krog": {
        "name": "Krog: Caveman Stress Relief",
        "icon": PL % "vMjdjoHlemN3kQSCp13_SDLQ7jFMx2CPdaeStYVXHySU-NFSlIuxtX2i_4VjFrzdVbjKvTjVy-yrIxrZKBv9",
        "en": {
            "collect": [
                "<b>No personal information.</b> Krog has no accounts and we do not collect your name, email or phone number.",
                "<b>No ads and no analytics.</b> The app contains no advertising or analytics libraries and does not send your data to any server of ours.",
            ],
            "local": ["Your game state (shells, items you unlocked), cave-wall drawings, language and sound settings."],
            "perms": [
                "<b>Vibration</b> — for haptic feedback while you smash stones.",
                "<b>Internet</b> — declared by the app framework; Krog does not use it to send your data anywhere.",
            ],
            "services": ["Krog has no ads and no real-money purchases. The in-game shop uses shells you earn by playing. "
                         "The home-screen widget only shows a saying from the app and reads no data from your device."],
            "children": "Krog is a general-audience app and is not directed to children under 13.",
        },
        "vi": {
            "collect": [
                "<b>Không thu thập thông tin cá nhân.</b> Krog không có tài khoản và chúng tôi không thu thập họ tên, email hay số điện thoại của bạn.",
                "<b>Không quảng cáo, không phân tích.</b> Ứng dụng không chứa thư viện quảng cáo hay phân tích và không gửi dữ liệu của bạn tới máy chủ nào của chúng tôi.",
            ],
            "local": ["Trạng thái trò chơi (số sò, vật phẩm đã mở khóa), hình vẽ trên vách hang, cài đặt ngôn ngữ và âm thanh."],
            "perms": [
                "<b>Rung</b> — để phản hồi xúc giác khi bạn đập đá.",
                "<b>Internet</b> — do khung ứng dụng khai báo; Krog không dùng nó để gửi dữ liệu của bạn đi đâu cả.",
            ],
            "services": ["Krog không có quảng cáo và không có giao dịch mua bằng tiền thật. Tiệm trong game dùng số sò bạn kiếm được khi chơi. "
                         "Widget màn hình chính chỉ hiển thị một câu nói trong ứng dụng và không đọc dữ liệu nào từ thiết bị."],
            "children": "Krog là ứng dụng cho mọi đối tượng và không nhắm tới trẻ em dưới 13 tuổi.",
        },
    },
    # ------------------------------------------------------------------ Little Passport
    "ho-chieu-nhi": {
        "name": "Little Passport (Hộ Chiếu Nhí)",
        "icon": "../../assets/ho-chieu-nhi.png",
        "en": {
            "collect": [
                "<b>The app collects no personal information from the child.</b> No account or sign-in; no access to contacts, location, camera, microphone, photos or files.",
                "<b>Ad library data (Google Mobile Ads SDK).</b> When ads are shown, Google may automatically collect the IP address (Google may estimate general location), interactions with the app and ads, diagnostic information, and technical device or app identifiers, for advertising, analytics and fraud prevention. Sent over encrypted connections.",
                "<b>No advertising ID.</b> The app does not use or request the advertising ID, and has no analytics library other than Google’s ad library.",
                "<b>Purchases.</b> One optional one-time purchase (Premium) through Google Play, behind the parent gate. Google Play handles payment; we receive no card or payment information.",
            ],
            "local": [
                "The child’s name (typed by the child or a parent; it can be left blank or be a nickname), chosen character and hat. We recommend not entering a full legal name.",
                "Play progress: countries visited, games completed, miles flown, stamps, certificates, quiz answers.",
                "Settings (language, sound, play-time limit) and whether Premium was bought and which countries are unlocked.",
                "All of this stays <b>only in the device’s storage</b> and is never sent to us, to Google or to anyone else.",
            ],
            "perms": ["The app requests no sensitive permissions and does not request the advertising ID permission."],
            "services": [
                "<b>Ads.</b> Ads are served by Google AdMob in child-directed mode: no personalised ads, no interest-based ads or remarketing, no tracking to target ads, and content limited to a level suitable for all ages. Ads are clearly separated from app content.",
                "Interstitial ads appear only at a natural pause after a child earns a stamp, never in the middle of play. Rewarded ads run only when a parent chooses to watch one to unlock a country, behind the parent gate. Buying Premium removes all ads. The games work offline; with no connection there are no ads and nothing is sent.",
            ],
            "children": "Little Passport is made for children aged 4–8 and designed to meet Google Play’s Designed for Families programme. We do not collect children’s personal information. "
                        "The parent area (play-time limit, progress report, progress reset, purchases) sits behind a verification gate. Parents should sit with the child for the first use.",
            "extra": [("Parent controls and deleting data",
                       "To delete progress, open the Parent area, choose “Start over” and confirm twice (certificates and the child’s profile are kept). "
                       "To delete everything, uninstall the app or go to device Settings, Apps, Little Passport, then Clear data. "
                       "Operating-system backups (such as Android backup to Google), if enabled by the parent, may include this app’s data; we do not receive those backups.")],
        },
        "vi": {
            "collect": [
                "<b>Ứng dụng không thu thập thông tin cá nhân của bé.</b> Không tài khoản hay đăng nhập; không xin quyền danh bạ, vị trí, camera, micro, ảnh hay tệp.",
                "<b>Dữ liệu của thư viện quảng cáo (Google Mobile Ads SDK).</b> Khi hiển thị quảng cáo, Google có thể tự động thu thập địa chỉ IP (Google có thể ước lượng vị trí chung), tương tác với ứng dụng và quảng cáo, thông tin chẩn đoán, và mã định danh kỹ thuật của thiết bị hay ứng dụng, dùng cho quảng cáo, phân tích và chống gian lận. Dữ liệu truyền qua kết nối mã hóa.",
                "<b>Không dùng mã quảng cáo.</b> Ứng dụng không dùng hay xin quyền mã quảng cáo (Advertising ID), và không có thư viện phân tích nào ngoài thư viện quảng cáo của Google.",
                "<b>Giao dịch mua.</b> Một gói mua một lần tùy chọn (Premium) qua Google Play, sau cổng phụ huynh. Google Play xử lý thanh toán; chúng tôi không nhận thông tin thẻ hay thanh toán.",
            ],
            "local": [
                "Tên bé (do bé hoặc phụ huynh nhập, có thể để trống hoặc dùng tên gọi ở nhà), nhân vật và chiếc mũ đã chọn. Khuyên không nhập họ tên đầy đủ.",
                "Tiến độ chơi: nước đã đến, trò đã hoàn thành, số dặm bay, con dấu, chứng nhận, câu đố đã trả lời.",
                "Cài đặt (ngôn ngữ, âm thanh, giới hạn thời gian chơi), trạng thái đã mua Premium và các nước đã mở khóa.",
                "Tất cả chỉ nằm <b>trong bộ nhớ của thiết bị</b> và không bao giờ được gửi cho chúng tôi, cho Google hay bất kỳ ai.",
            ],
            "perms": ["Ứng dụng không yêu cầu quyền nhạy cảm nào và không xin quyền mã quảng cáo."],
            "services": [
                "<b>Quảng cáo.</b> Quảng cáo do Google AdMob phân phối ở chế độ dành cho trẻ em: không quảng cáo cá nhân hóa, không quảng cáo theo sở thích hay tiếp thị lại, không theo dõi để nhắm quảng cáo, nội dung giới hạn ở mức phù hợp mọi lứa tuổi. Quảng cáo được tách rõ khỏi nội dung ứng dụng.",
                "Quảng cáo xen kẽ chỉ hiện ở điểm nghỉ sau khi bé nhận con dấu, không bao giờ giữa lúc chơi. Quảng cáo thưởng chỉ chạy khi phụ huynh chủ động bấm xem để mở khóa một nước, sau cổng phụ huynh. Mua Premium sẽ bỏ toàn bộ quảng cáo. Các trò chơi chạy được khi không có mạng; khi không có mạng thì không có quảng cáo và không có dữ liệu nào được gửi.",
            ],
            "children": "Hộ Chiếu Nhí dành cho trẻ 4–8 tuổi và được thiết kế theo chương trình Designed for Families của Google Play. Chúng tôi không thu thập thông tin cá nhân của trẻ. "
                        "Khu vực phụ huynh (giới hạn giờ chơi, báo cáo, xóa tiến độ, mua hàng) có cổng xác minh. Phụ huynh nên ngồi cùng bé ở lần dùng đầu tiên.",
            "extra": [("Quyền của phụ huynh và xóa dữ liệu",
                       "Xóa tiến độ: vào Khu phụ huynh, chọn “Chơi lại từ đầu” và xác nhận hai bước (chứng nhận và hồ sơ của bé được giữ lại). "
                       "Xóa toàn bộ: gỡ ứng dụng, hoặc vào Cài đặt thiết bị, Ứng dụng, Hộ Chiếu Nhí, rồi Xóa dữ liệu. "
                       "Sao lưu của hệ điều hành (như sao lưu Android lên Google), nếu phụ huynh bật, có thể gồm dữ liệu của ứng dụng; chúng tôi không nhận các bản sao lưu đó.")],
        },
    },
    # ------------------------------------------------------------------ Smart Sight
    "smart-sight": {
        "name": "Smart Sight Assistant",
        "icon": None,
        "en": {
            "collect": [
                "<b>Camera frames.</b> Used only when you scan a label. Text is read on your device by a text-recognition model that ships inside the app. A captured frame is held in memory only and erased after reading; the app never saves photos.",
                "<b>Label text and your choices.</b> Text read from labels, your allergy list and your settings stay on your phone.",
                "<b>No account, no analytics, no ads.</b> The app has no sign-in, no analytics or crash-reporting library and no advertising.",
                "<b>Subscription information.</b> Plans are sold through Google Play. We never see your payment details; the app checks with Google Play whether your plan is active.",
            ],
            "local": ["Recent labels, allergy list, saved plan state, purchase notes, trial reminder and settings. Android auto-backup and phone-to-phone transfer are turned off for this app, so this data is not copied to Google or another phone."],
            "perms": [
                "<b>Camera</b> — to scan labels. You can revoke it any time in Android settings.",
                "<b>Notifications</b> — one local reminder before your free trial ends. It is created on your phone; nothing is sent from a server.",
                "The app itself does not hold the Internet permission, so it cannot send your labels or photos anywhere. Google Play handles purchases separately.",
            ],
            "services": ["<b>Subscriptions.</b> After a free trial you can subscribe monthly or yearly through Google Play Billing. Your plan is kept by Google Play: “Delete my data” in the app does not cancel a subscription; cancel it in Google Play."],
            "children": "Smart Sight Assistant is for adults, including older adults and their caregivers, and is not directed to children.",
            "extra": [("Not medical advice",
                       "Smart Sight Assistant reads printed text aloud to help you see it. It does not give dosing advice, check drug interactions, or tell you whether something is safe to take or eat. "
                       "Always check the original label and ask a pharmacist or doctor when unsure.")],
        },
        "vi": {
            "collect": [
                "<b>Khung hình từ camera.</b> Chỉ dùng khi bạn quét nhãn. Chữ được đọc ngay trên thiết bị bằng mô hình nhận dạng chữ nằm sẵn trong ứng dụng. Khung hình chụp chỉ giữ trong bộ nhớ và bị xóa sau khi đọc; ứng dụng không bao giờ lưu ảnh.",
                "<b>Nội dung nhãn và lựa chọn của bạn.</b> Chữ đọc từ nhãn, danh sách dị ứng và cài đặt của bạn nằm trên điện thoại.",
                "<b>Không tài khoản, không phân tích, không quảng cáo.</b> Ứng dụng không có đăng nhập, không có thư viện phân tích hay báo lỗi, và không có quảng cáo.",
                "<b>Thông tin đăng ký gói.</b> Các gói được bán qua Google Play. Chúng tôi không thấy thông tin thanh toán; ứng dụng hỏi Google Play xem gói của bạn còn hiệu lực không.",
            ],
            "local": ["Nhãn gần đây, danh sách dị ứng, trạng thái gói đã lưu, ghi chú giao dịch, nhắc nhở dùng thử và cài đặt. Tính năng tự sao lưu của Android và chuyển dữ liệu giữa hai điện thoại đã tắt cho ứng dụng này, nên dữ liệu không được chép lên Google hay sang máy khác."],
            "perms": [
                "<b>Camera</b> — để quét nhãn. Bạn có thể thu hồi quyền bất kỳ lúc nào trong cài đặt Android.",
                "<b>Thông báo</b> — một nhắc nhở cục bộ trước khi hết dùng thử. Nó được tạo trên điện thoại; không có gì được gửi từ máy chủ.",
                "Bản thân ứng dụng không có quyền Internet nên không thể gửi nhãn hay ảnh của bạn đi đâu. Google Play xử lý giao dịch riêng.",
            ],
            "services": ["<b>Đăng ký gói.</b> Sau thời gian dùng thử miễn phí, bạn có thể đăng ký theo tháng hoặc năm qua Google Play Billing. Gói do Google Play giữ: “Xóa dữ liệu của tôi” trong ứng dụng không hủy gói; hãy hủy trong Google Play."],
            "children": "Smart Sight Assistant dành cho người lớn, gồm người lớn tuổi và người chăm sóc, không nhắm tới trẻ em.",
            "extra": [("Không phải lời khuyên y tế",
                       "Smart Sight Assistant đọc to chữ in để giúp bạn nhìn rõ. Ứng dụng không đưa ra liều dùng, không kiểm tra tương tác thuốc, và không cho biết một thứ có an toàn để uống hay ăn hay không. "
                       "Luôn kiểm tra nhãn gốc và hỏi dược sĩ hoặc bác sĩ khi chưa chắc.")],
        },
    },
}

UI = {
    "en": {
        "title": "Privacy Policy", "updated": "Last updated", "back": "← All apps",
        "h_summary": "Summary", "h_collect": "Information we collect", "h_local": "Data stored on your device", "h_perms": "Permissions",
        "h_services": "Ads, purchases and third-party services", "h_children": "Children’s privacy", "h_share": "Sharing and selling data",
        "h_keep": "Retention and deletion", "h_sec": "Security", "h_change": "Changes to this policy", "h_contact": "Contact",
        "summary": "This policy explains how {dev} handles information in {app}. We keep it short and say plainly what the app does and does not do.",
        "share": "We do not sell your personal information. We share data with third parties only through the service providers described above, and only as needed to run the app.",
        "keep": "Data stored by the app lives on your device. Clearing the app’s storage or uninstalling the app deletes it. "
                "Data collected by Google or other providers described above is kept under their own policies. To ask about any data we may hold about you, contact us below.",
        "sec": "We rely on the security of the Android platform and Google Play. No method of electronic storage is perfectly secure.",
        "change": "If we change this policy we will post the new version on this page and update the date above.",
        "contact": "Questions or requests: ",
    },
    "vi": {
        "title": "Chính sách quyền riêng tư", "updated": "Cập nhật lần cuối", "back": "← Tất cả ứng dụng",
        "h_summary": "Tóm tắt", "h_collect": "Thông tin chúng tôi thu thập", "h_local": "Dữ liệu lưu trên thiết bị", "h_perms": "Quyền truy cập",
        "h_services": "Quảng cáo, giao dịch mua và dịch vụ bên thứ ba", "h_children": "Quyền riêng tư của trẻ em", "h_share": "Chia sẻ và bán dữ liệu",
        "h_keep": "Lưu trữ và xóa dữ liệu", "h_sec": "Bảo mật", "h_change": "Thay đổi chính sách", "h_contact": "Liên hệ",
        "summary": "Chính sách này giải thích cách {dev} xử lý thông tin trong ứng dụng {app}. Chúng tôi viết ngắn gọn và nói rõ ứng dụng làm gì, không làm gì.",
        "share": "Chúng tôi không bán thông tin cá nhân của bạn. Dữ liệu chỉ đến bên thứ ba qua các nhà cung cấp dịch vụ nêu ở trên, và chỉ khi cần để ứng dụng hoạt động.",
        "keep": "Dữ liệu do ứng dụng lưu nằm trên thiết bị của bạn. Xóa dữ liệu ứng dụng hoặc gỡ cài đặt sẽ xóa chúng. "
                "Dữ liệu do Google hoặc nhà cung cấp khác nêu ở trên thu thập được giữ theo chính sách riêng của họ. Nếu muốn hỏi về dữ liệu chúng tôi có thể đang giữ, hãy liên hệ bên dưới.",
        "sec": "Chúng tôi dựa vào cơ chế bảo mật của nền tảng Android và Google Play. Không phương thức lưu trữ điện tử nào an toàn tuyệt đối.",
        "change": "Nếu thay đổi chính sách, chúng tôi sẽ đăng bản mới trên trang này và cập nhật ngày ở trên.",
        "contact": "Câu hỏi hoặc yêu cầu: ",
    },
}

CSS = """\
:root{--bg:#fbf8f3;--surface:#fff;--ink:#1b1613;--muted:#6a5f57;--line:#e9e1d6;--accent:#ff5a1f;--blue:#2f6bff}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14110f;--surface:#1f1a17;--ink:#f6efe8;--muted:#b3a79d;--line:#332c27;--blue:#7fa6ff}}
:root[data-theme=dark]{--bg:#14110f;--surface:#1f1a17;--ink:#f6efe8;--muted:#b3a79d;--line:#332c27;--blue:#7fa6ff}
*{box-sizing:border-box;margin:0}
body{background:var(--bg);color:var(--ink);font:16px/1.7 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{width:min(760px,100% - 32px);margin-inline:auto}
header{border-bottom:1px solid var(--line)}
.bar{display:flex;justify-content:space-between;align-items:center;height:60px;gap:12px}
.bar a{color:var(--muted);text-decoration:none;font-weight:600;font-size:.95rem}
.bar a:hover{color:var(--ink)}
.chip{border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;padding:6px 14px;font:600 .85rem system-ui;cursor:pointer;min-height:36px}
.chip:hover{border-color:var(--accent)}
.head{display:flex;gap:18px;align-items:center;padding:40px 0 8px}
.head img,.head .noicon{width:72px;height:72px;border-radius:18px;border:1px solid var(--line);flex:none}
.head .noicon{display:grid;place-items:center;background:var(--surface);font-size:2rem}
h1{font-size:clamp(1.7rem,4.5vw,2.4rem);line-height:1.15;letter-spacing:-.02em}
.meta{color:var(--muted);font-size:.92rem;margin-top:4px}
h2{font-size:1.2rem;margin:36px 0 8px}
p,ul{margin-bottom:12px}
ul{padding-left:1.25rem}li{margin-bottom:6px}
a{color:var(--blue)}
footer{margin:56px 0 40px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:.9rem}
html[lang=vi] [lang=en],html[lang=en] [lang=vi]{display:none}
a:focus-visible,button:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
"""


def e(s):
    return html.escape(s, quote=False)


def ul(items):
    # items may contain trusted inline <b> tags written above
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def block(app, lang):
    d, u = app[lang], UI[lang]
    o = [f'<div lang="{lang}">']
    o.append(f'<h2>{u["h_summary"]}</h2><p>{e(u["summary"].format(dev=DEVELOPER, app=app["name"]))}</p>')
    o.append(f'<h2>{u["h_collect"]}</h2>{ul(d["collect"])}')
    o.append(f'<h2>{u["h_local"]}</h2>{ul(d["local"])}')
    o.append(f'<h2>{u["h_perms"]}</h2>{ul(d["perms"])}')
    o.append(f'<h2>{u["h_services"]}</h2>' + "".join(f"<p>{x}</p>" for x in d["services"]))
    o.append(f'<h2>{u["h_children"]}</h2><p>{e(d["children"])}</p>')
    for head, text in d.get("extra", []):
        o.append(f"<h2>{e(head)}</h2><p>{e(text)}</p>")
    o.append(f'<h2>{u["h_share"]}</h2><p>{e(u["share"])}</p>')
    o.append(f'<h2>{u["h_keep"]}</h2><p>{e(u["keep"])}</p>')
    o.append(f'<h2>{u["h_sec"]}</h2><p>{e(u["sec"])}</p>')
    o.append(f'<h2>{u["h_change"]}</h2><p>{e(u["change"])}</p>')
    o.append(f'<h2>{u["h_contact"]}</h2><p>{u["contact"]}<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>')
    o.append("</div>")
    return "\n".join(o)


def page(slug, app):
    icon = (f'<img src="{app["icon"]}" alt="" width="72" height="72">' if app["icon"]
            else '<div class="noicon" aria-hidden="true">👁</div>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(app["name"])} — Privacy Policy</title>
<meta name="description" content="Privacy policy for {e(app["name"])} by {DEVELOPER}.">
<meta name="robots" content="index,follow">
<link rel="stylesheet" href="../policy.css">
</head>
<body>
<header><div class="wrap bar">
  <a href="../../#apps" id="back">{UI["en"]["back"]}</a>
  <button class="chip" id="lang" type="button" aria-label="Switch language">Tiếng Việt</button>
</div></header>
<main class="wrap">
  <div class="head">
    {icon}
    <div>
      <h1><span lang="en">{UI["en"]["title"]}</span><span lang="vi">{UI["vi"]["title"]}</span></h1>
      <div class="meta">{e(app["name"])} · <span lang="en">{UI["en"]["updated"]}</span><span lang="vi">{UI["vi"]["updated"]}</span>: {LAST_UPDATED}</div>
    </div>
  </div>
{block(app, "en")}
{block(app, "vi")}
</main>
<footer><div class="wrap">© <span id="yr"></span> {DEVELOPER} · <a href="{PLAY_DEV}" rel="noopener">Google Play</a></div></footer>
<script>
(function(){{
  var r=document.documentElement,b=document.getElementById("lang"),back=document.getElementById("back");
  function s(f){{try{{return f()}}catch(e){{}}}}
  function set(l){{r.lang=l;b.textContent=l==="vi"?"English":"Tiếng Việt";back.textContent=l==="vi"?"{UI["vi"]["back"]}":"{UI["en"]["back"]}";
    document.title="{e(app["name"])} — "+(l==="vi"?"{UI["vi"]["title"]}":"{UI["en"]["title"]}");s(function(){{localStorage.setItem("tk-lang",l)}})}}
  var l=s(function(){{return localStorage.getItem("tk-lang")}})||((navigator.language||"").toLowerCase().indexOf("vi")===0?"vi":"en");
  set(l);b.addEventListener("click",function(){{set(r.lang==="vi"?"en":"vi")}});
  var t=s(function(){{return localStorage.getItem("tk-theme")}});if(t)r.dataset.theme=t;
  document.getElementById("yr").textContent=new Date().getFullYear();
}})();
</script>
</body>
</html>
"""


def main():
    out = ROOT / "privacy"
    out.mkdir(exist_ok=True)
    (out / "policy.css").write_text(CSS, encoding="utf-8")
    for slug, app in APPS.items():
        d = out / slug
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(slug, app), encoding="utf-8")
        print("wrote", d / "index.html")


if __name__ == "__main__":
    main()
