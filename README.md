
---

## 🛠️ Technologies & Tools

- 🐍 Python 3.x  
- 💻 VS Code  
- 🌐 Git & GitHub  
- 🧠 LeetCode (for DSA practice)  

---

## 📈 GitHub Stats

> (Replace `yourusername` with your actual GitHub username)

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=yourusername&show_icons=true&theme=tokyonight)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=yourusername&layout=compact&theme=tokyonight)

---

## 🔥 Contribution Streak

![GitHub Streak](https://streak-stats.demolab.com/?user=yourusername&theme=tokyonight)

---

## 📌 Why This Repository?

Consistency builds confidence.  
Confidence builds skill.  
Skill builds career.  

This repository helps me track my growth, stay disciplined, and prepare effectively for placements and real-world software development.

---

## 🤝 Connect With Me

If you are also learning Python, feel free to fork this repository and start your own daily coding journey.

Let’s grow together 🚀  

---

⭐ If you find this repository helpful, don’t forget to star it!
"""

file_path = "/mnt/data/README_Daily_Python_Kabir_Sawant.md"

# Save as standalone markdown file using pypandoc
pypandoc.convert_text(readme_content, 'md', format='md', outputfile=file_path, extra_args=['--standalone'])

file_path
