# 🚨 Ransomware Detection Simulator

## 📌 Project Overview
This project simulates a ransomware detection system in a healthcare environment.  
It demonstrates real-time monitoring of files for suspicious activity, helping to detect potential ransomware attacks before they cause damage.

Ransomware is one of the most dangerous threats in healthcare because it can encrypt patient data and disrupt critical services.

---

## 🔒 Security Features

✅ **Real-Time Monitoring**  
The program watches a folder for any file changes.

✅ **Suspicious Activity Detection**  
Flags unusual behavior, such as multiple rapid file modifications, which may indicate ransomware.

✅ **Behavioral Alerts**  
Logs all suspicious activity and triggers high alerts when mass changes occur.

✅ **Logging**  
All events are logged in `alert_log.txt` for audit and analysis.

---

## 🛠 Technologies Used
- Python  
- Watchdog library for file monitoring  
- File logging  

---

## ▶️ How to Run

1. Clone the repository  
2. Create a folder called `protected_folder` inside the project folder  
3. Place any sample files you want to monitor inside `protected_folder`  
4. Run the program: python analyzer.py


Modify or create files in the folder to test alerts. After multiple rapid changes, a high alert will trigger.

---

## 🧠 Cybersecurity Concepts Demonstrated
- Real-time monitoring  
- Behavioral threat detection  
- Ransomware attack simulation  
- Logging and alerting  

---

## 🚀 Future Improvements
- Integration with databases for larger systems  
- Email or system alerts for high-risk events  
- More advanced anomaly detection  
- GUI interface for easier monitoring  

---

## 👨‍💻 Author
**Lehlogonolo Mpye**  
Aspiring Cybersecurity Professional focused on defending sensitive systems and critical infrastructure.

