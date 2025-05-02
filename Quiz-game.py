import tkinter as tk
from tkinter import messagebox
import random
import csv
import os

# ---------------------- الأسئلة بالعربية --------------------------
questions_ar = [
    {
        "question": "ما هي أفضل طريقة لحماية كلمة المرور الخاصة بك؟",
        "options": ["مشاركتها مع الأصدقاء", "استخدام كلمة مرور قوية وفريدة", "تدوينها على الورق"],
        "answer": "استخدام كلمة مرور قوية وفريدة"
    },
    {
        "question": "ما الذي يجب فعله عند تلقي رسالة مشبوهة؟",
        "options": ["فتح الرابط فورًا", "حذف الرسالة أو التحقق منها", "إعادة إرسالها للأصدقاء"],
        "answer": "حذف الرسالة أو التحقق منها"
    },
    {
        "question": "ما هو التصرف الصحيح عند استخدام الهاتف في الأماكن العامة؟",
        "options": ["ترك الهاتف دون قفل", "الحرص على عدم كشف المعلومات الشخصية", "التقاط صور للغرباء"],
        "answer": "الحرص على عدم كشف المعلومات الشخصية"
    },
    {
        "question": "ماذا يجب أن أفعل لجعل كلمة المرور الخاصة بي قوية؟",
        "options": ["استخدام اسم العائلة أو تاريخ الميلاد", "استخدام خليط من الحروف، الأرقام والرموز", "إعادة استخدام نفس الكلمة في كل المواقع"],
        "answer": "استخدام خليط من الحروف، الأرقام والرموز"
    },
    {
        "question": "ماذا تفعل إذا تلقيت بريدًا إلكترونيًا من جهة غير معروفة؟",
        "options": ["فتح الرابط مباشرة", "لا تفتح الرابط وتراجع العنوان", "الرد على المرسل بالسؤال عن هويته"],
        "answer": "لا تفتح الرابط وتراجع العنوان"
    },
    {
        "question": "ماذا يجب عليك أن تفعل عند استخدام شبكة واي فاي عامة (مثلًا في المقاهي)؟",
        "options": ["إدخال معلوماتك البنكية بشكل طبيعي", "تجنب زيارة المواقع الحساسة", "تحميل ملفات كبيرة بسرعة"],
        "answer": "تجنب زيارة المواقع الحساسة"
    },
    {
        "question": "ما معنى التصيد الإلكتروني ؟",
        "options": ["لعبة جديدة على Play Store", "خداع الأشخاص للحصول على معلوماتهم الحساسة", "موقع حكومي رسمي"],
        "answer": "خداع الأشخاص للحصول على معلوماتهم الحساسة"
    },
    {
    "question": "كيف يمكن أن يستفيد الهاكر من تطبيق قديم غير محدث؟",
    "options": ["قد يجد ثغرات أمنية ليست موجودة في الإصدارات الجديدة","يستطيع تغيير لغة التطبيق","يتحكم في حجم الشاشة"],
    "answer": "قد يجد ثغرات أمنية ليست موجودة في الإصدارات الجديدة"
    },
    {
        "question": "ماذا يجب أن أفعل قبل مشاركة صورة تحتوي على أشخاص آخرين؟",
        "options": ["مشاركتها مباشرة", "سؤالهم إذا كانوا موافقين", "تعديلها بالفلاتر أولاً"],
        "answer": "سؤالهم إذا كانوا موافقين"
    },
    {
        "question": "هل تحمل تطبيقًا ذو تقييمات ضعيفة جدًا؟",
        "options": ["نعم، فقط لتجربته", "لا، تراجع وتأكد", "اسأل صديقك عنه أولاً"],
        "answer": "لا، تراجع وتأكد"
    },
    {
        "question": "هل تثق بعرض مغري على الإنترنت يقول لك 'ربحت هاتفًا، فقط أدخل معلوماتك'؟",
        "options": ["إدخال المعلومات", "الشك في العرض وحذف الرسالة", "مشاركته على وسائل التواصل"],
        "answer": "الشك في العرض وحذف الرسالة"
    },
    {
    "question": "لماذا يُنصح بعدم تحميل برامج من مواقع غير موثوقة؟",
    "options": ["لأنها قد تحتوي على فيروسات أو برمجيات ضارة","لأنها تأخذ مساحة كبيرة فقط","لأنها تُغلق الجهاز تلقائيًا"],
    "answer": "لأنها قد تحتوي على فيروسات أو برمجيات ضارة"
    },
    {
        "question": "ماذا يجب أن أفعل عندما أريد بيع هاتفي؟",
        "options": ["إعطائه مباشرة", "مسح جميع البيانات وإعادة ضبط المصنع", "نزع بطاقة SIM فقط"],
        "answer": "مسح جميع البيانات وإعادة ضبط المصنع"
    }
]

# ---------------------- الأسئلة بالفرنسية --------------------------
questions_fr = [
    {
        "question": "Quelle est la meilleure façon de protéger votre mot de passe ?",
        "options": ["Le partager avec des amis", "Utiliser un mot de passe fort et unique", "L'écrire sur du papier"],
        "answer": "Utiliser un mot de passe fort et unique"
    },
    {
        "question": "Que faire si vous recevez un message suspect ?",
        "options": ["Ouvrir le lien immédiatement", "Supprimer le message ou vérifier sa source", "Le transférer à vos amis"],
        "answer": "Supprimer le message ou vérifier sa source"
    },
    {
        "question": "Quel est le bon comportement avec un téléphone en public ?",
        "options": ["Laisser le téléphone sans verrou", "Faire attention à ne pas révéler ses infos personnelles", "Prendre des photos des inconnus"],
        "answer": "Faire attention à ne pas révéler ses infos personnelles"
    },
    {
        "question": "Comment rendre votre mot de passe plus fort ?",
        "options": ["Utiliser votre nom ou date de naissance", "Utiliser un mélange de lettres, chiffres et symboles", "Réutiliser le même mot de passe partout"],
        "answer": "Utiliser un mélange de lettres, chiffres et symboles"
    },
    {
        "question": "Que faire si vous recevez un email d’un expéditeur inconnu ?",
        "options": ["Ouvrir le lien directement", "Ne pas ouvrir le lien et vérifier l'adresse", "Répondre pour demander son identité"],
        "answer": "Ne pas ouvrir le lien et vérifier l'adresse"
    },
    {
        "question": "Que faire lors de l'utilisation d'un Wi-Fi public (comme dans un café) ?",
        "options": ["Entrer vos infos bancaires normalement", "Éviter les sites sensibles", "Télécharger de gros fichiers"],
        "answer": "Éviter les sites sensibles"
    },
    {
        "question": "Que signifie le phishing ?",
        "options": ["Un nouveau jeu sur Play Store", "Tromper les gens pour obtenir leurs infos sensibles", "Un site officiel du gouvernement"],
        "answer": "Tromper les gens pour obtenir leurs infos sensibles"
    },
    {
        "question": "Comment un hacker peut-il profiter d'une vieille application non mise à jour ?",
        "options": ["Il peut y trouver des failles absentes des nouvelles versions", "Il peut changer la langue de l'app", "Il peut contrôler la taille de l'écran"],
        "answer": "Il peut y trouver des failles absentes des nouvelles versions"
    },
    {
        "question": "Que faire avant de partager une photo contenant d'autres personnes ?",
        "options": ["La partager directement", "Leur demander leur accord", "La modifier avec des filtres d'abord"],
        "answer": "Leur demander leur accord"
    },
    {
        "question": "Téléchargeriez-vous une application avec une très mauvaise note ?",
        "options": ["Oui, juste pour tester", "Non, mieux vaut vérifier d'abord", "Demander l'avis d’un ami"],
        "answer": "Non, mieux vaut vérifier d'abord"
    },
    {
        "question": "Faire confiance à une offre en ligne disant : 'Vous avez gagné un téléphone, entrez vos infos' ?",
        "options": ["Entrer les infos", "Se méfier et supprimer le message", "La partager sur les réseaux"],
        "answer": "Se méfier et supprimer le message"
    },
    {
        "question": "Pourquoi ne pas télécharger de logiciels depuis des sites non fiables ?",
        "options": ["Ils peuvent contenir des virus ou logiciels malveillants", "Ils prennent trop d’espace", "Ils éteignent l’appareil automatiquement"],
        "answer": "Ils peuvent contenir des virus ou logiciels malveillants"
    },
    {
        "question": "Que faire avant de vendre son téléphone ?",
        "options": ["Le donner directement", "Supprimer toutes les données et réinitialiser", "Juste retirer la carte SIM"],
        "answer": "Supprimer toutes les données et réinitialiser"
    }
]



# ---------------------- التطبيق الرئيسي --------------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ Quiz Game - Sécurité Numérique")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.name = ""
        self.language = ""
        self.score = 0
        self.q_index = 0
        self.questions = []
        self.correct_answer = ""
        self.question_order = []

        # نبدأ باختيار اللغة أولاً
        self.choose_language()

    def choose_language(self):
        self.clear_window()
        tk.Label(self.root, text="🌐 اختر اللغة / Choisissez la langue :", font=("Arial", 16)).pack(pady=20)

        ar_button = tk.Button(self.root, text="🇲🇦 العربية", font=("Arial", 14), width=20, command=lambda: self.set_language("ar"))
        ar_button.pack(pady=10)
        # إضافة تأثير الماوس على الأزرار
        self.add_hover_effect(ar_button)
        
        fr_button = tk.Button(self.root, text="🇫🇷 Français", font=("Arial", 14), width=20, command=lambda: self.set_language("fr"))
        fr_button.pack(pady=10)
        # إضافة تأثير الماوس على الأزرار
        self.add_hover_effect(fr_button)

    def set_language(self, lang):
        self.language = lang
        self.questions = questions_ar if lang == "ar" else questions_fr
        self.setup_name_screen()

    def setup_name_screen(self):
        self.clear_window()
        
        # عرض النص حسب اللغة المختارة
        name_prompt = ": أدخل اسمك" if self.language == "ar" else " Entrez votre nom :"
        button_text = "التالي" if self.language == "ar" else "Suivant"
        
        tk.Label(self.root, text=name_prompt, font=("Arial", 16)).pack(pady=20)
        self.name_entry = tk.Entry(self.root, font=("Arial", 16))
        self.name_entry.pack()

        next_button = tk.Button(self.root, text=button_text, font=("Arial", 14), bg="#4CAF50", fg="white", command=self.start_quiz)
        next_button.pack(pady=20)
        # إضافة تأثير الماوس على الزر
        self.add_hover_effect(next_button, bg_color="#4CAF50", hover_color="#45a049")

    def start_quiz(self):
        self.name = self.name_entry.get().strip()
        if not self.name:
            warning_text = "من فضلك أدخل اسمك" if self.language == "ar" else "Veuillez entrer votre nom."
            messagebox.showwarning("⚠️ Attention", warning_text)
            return
            
        self.q_index = 0
        self.score = 0
        
        # إنشاء ترتيب عشوائي للأسئلة
        self.question_order = list(range(len(self.questions)))
        random.shuffle(self.question_order)
        
        self.show_question()

    def show_question(self):
        if self.q_index >= len(self.questions):
            self.finish_quiz()
            return

        self.clear_window()
        current_q_idx = self.question_order[self.q_index]
        current_q = self.questions[current_q_idx]
        
        tk.Label(self.root, text=f"{current_q['question']}", wraplength=500, font=("Arial", 14)).pack(pady=30)

        # نسخ الخيارات وخلطها
        options = current_q['options'].copy()
        random.shuffle(options)
        
        # تتبع الإجابة الصحيحة
        self.correct_answer = current_q['answer']
        
        # إنشاء أزرار للخيارات
        self.buttons = []
        for option in options:
            btn = tk.Button(self.root, text=f"{option}", font=("Arial", 12), width=50,
                           command=lambda opt=option: self.check_answer(opt))
            btn.pack(pady=5)
            self.buttons.append(btn)
            # إضافة تأثير الماوس على كل زر خيار
            self.add_hover_effect(btn)

    def check_answer(self, chosen):
        if chosen == self.correct_answer:
            self.score += 1
        self.q_index += 1
        self.show_question()

    def finish_quiz(self):
        # حفظ النتيجة أولاً
        self.save_score()
        
        # الحصول على معلومات الترتيب
        rank, players = self.get_rank()
        
        self.clear_window()

        # --- العناوين ---
        title = "📊 النتيجة النهائية" if self.language == "ar" else "📊 Résultat final"
        name_text = f"الاسم: {self.name}" if self.language == "ar" else f"Nom : {self.name}"
        score_text = f"النقاط: {self.score} / {len(self.questions)}" if self.language == "ar" else f"Score : {self.score} / {len(self.questions)}"
        rank_text = f"الرتبة: {rank} من {len(players)}" if self.language == "ar" else f"Classement : {rank} sur {len(players)}"
        table_title = "📋 جدول الترتيب" if self.language == "ar" else "📋 Tableau des scores"

        tk.Label(self.root, text=title, font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text=name_text, font=("Arial", 14)).pack(pady=5)
        tk.Label(self.root, text=score_text, font=("Arial", 14)).pack(pady=5)
        tk.Label(self.root, text=rank_text, font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=table_title, font=("Arial", 14, "underline")).pack(pady=10)

        # --- عرض الجدول ---
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10)

        headers = ["#", "الاسم", "النقاط"] if self.language == "ar" else ["#", "Nom", "Score"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=("Arial", 12, "bold"), width=15, borderwidth=1, relief="solid").grid(row=0, column=col)

        for i, p in enumerate(players[:10], start=1):  # عرض أعلى 10
            # تحديد ما إذا كان هذا هو اللاعب الحالي
            is_current_player = (p["name"] == self.name and p["score"] == self.score)
            
            # تعيين الألوان والتنسيق بناءً على ما إذا كان هذا هو اللاعب الحالي
            bg_color = "#ffff99" if is_current_player else "white"  # خلفية صفراء للاعب الحالي
            fg_color = "#000000" if is_current_player else "#000000"  # لون النص الأسود للجميع
            font_style = ("Arial", 12, "bold") if is_current_player else ("Arial", 12)  # نص غامق للاعب الحالي
            
            # إنشاء تسميات الصف مع تنسيق خاص
            tk.Label(table_frame, text=str(i), font=font_style, width=15, 
                    borderwidth=1, relief="solid", bg=bg_color, fg=fg_color).grid(row=i, column=0)
            tk.Label(table_frame, text=p["name"], font=font_style, width=15, 
                    borderwidth=1, relief="solid", bg=bg_color, fg=fg_color).grid(row=i, column=1)
            tk.Label(table_frame, text=str(p["score"]), font=font_style, width=15, 
                    borderwidth=1, relief="solid", bg=bg_color, fg=fg_color).grid(row=i, column=2)
            
            # إضافة تأثير وميض للاعب الحالي
            if is_current_player:
                self.flash_row(table_frame, i, bg_color)

        # --- زر إعادة اللعب ---
        restart_text = "🔄 العب مرة أخرى" if self.language == "ar" else "🔄 Jouer à nouveau"
        restart_button = tk.Button(self.root, text=restart_text, font=("Arial", 14), bg="#4CAF50", fg="white", 
                 command=self.choose_language)
        restart_button.pack(pady=20)
        # إضافة تأثير الماوس على زر إعادة اللعب
        self.add_hover_effect(restart_button, bg_color="#4CAF50", hover_color="#45a049")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    # دالة إضافة تأثير عند تمرير المؤشر فوق الزر
    def add_hover_effect(self, button, bg_color=None, hover_color="#e0e0e0"):
        original_bg = bg_color if bg_color else button["background"]
        
        # تغيير اللون عند مرور المؤشر فوق الزر
        button.bind("<Enter>", lambda e: button.config(background=hover_color, cursor="hand2"))
        # إعادة اللون الأصلي عند خروج المؤشر من الزر
        button.bind("<Leave>", lambda e: button.config(background=original_bg))
        
    # دالة لإضافة تأثير الوميض للصف الحالي في الجدول
    def flash_row(self, table_frame, row_num, base_color):
        # الألوان التي سيتغير بينها الصف
        colors = ["#ffff99", "#fff066", "#ffff99"]  # تدرج ألوان أصفر
        labels = [widget for widget in table_frame.grid_slaves() if int(widget.grid_info()["row"]) == row_num]
        
        def flash_cycle(index=0):
            if index < len(colors) * 2:  # كرر دورة الألوان مرتين
                color = colors[index % len(colors)]
                for label in labels:
                    label.config(bg=color)
                # استدعاء الدالة مرة أخرى بعد 500 مللي ثانية
                self.root.after(500, lambda: flash_cycle(index + 1))

    def save_score(self):
        filename = "quiz_scores.csv"
        file_exists = os.path.isfile(filename)
        
        try:
            with open(filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["Name", "Score"])
                writer.writerow([self.name, self.score])
        except Exception as e:
            messagebox.showerror("Error", f"Could not save score: {str(e)}")

    def get_rank(self):
        filename = "quiz_scores.csv"
        players = []
        
        # إنشاء الملف إذا لم يكن موجودًا
        if not os.path.isfile(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score"])
        
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        players.append({"name": row["Name"], "score": int(row["Score"])})
                    except (ValueError, KeyError):
                        # تخطي الصفوف غير الصالحة
                        continue
                        
            # إضافة اللاعب الحالي إذا لم يكن موجودًا بالفعل في القائمة
            current_player = {"name": self.name, "score": self.score}
            if current_player not in players:
                players.append(current_player)
                
            # ترتيب حسب النقاط (الأعلى أولاً)
            players.sort(key=lambda x: x["score"], reverse=True)
            
            # البحث عن رتبة اللاعب
            for i, p in enumerate(players):
                if p["name"] == self.name and p["score"] == self.score:
                    return i + 1, players
                    
            return len(players), players
        except Exception as e:
            messagebox.showerror("Error", f"Could not read scores: {str(e)}")
            return 1, [{"name": self.name, "score": self.score}]


# ---------------------- تشغيل البرنامج --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()