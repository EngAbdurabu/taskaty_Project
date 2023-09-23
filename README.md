# taskaty_Project

this is a CLI app to mange your task 

## to use this app 
لعرض الملفات والمجلدات ضمن مجلد محدد:
ls -l {path}
استبدل {path} بمسار المجلد.

لعرض الملفات والمجلدات ضمن المجلد الحالي:
ls -l
لعرض المجلدات ضمن مجلد محدد:
dir {path}
استبدل {path} بمسار المجلد.

لعرض الملفات والمجلدات ضمن المجلد الحالي:
dir
لعرض الملفات والمجلدات باستخدام dir بطريقة مرتبة:
dir /w
إضافة مهمة جديدة من خلال تطبيق Taskaty:
taskaty add {task_name}
نستبدل {task_name} باسم المهمة.

لاستعراض المهام الموجودة حاليًّا وغير المنفذة بعد:
taskaty list
استعراض جميع المهام:
taskaty list -a
تنفيذ مهمة محددة:
taskaty check -t {task_id}
نستبدل {task_id} بمُعرّف المهمة.

حذف مهمة محددة:
taskaty remove -t {task_id}
حذف جميع المهام:
taskaty reset
