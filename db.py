import sqlite3
import time
from datetime import datetime

def update_loginstatus():
    """
    更新lwservice.db数据库中tOption表的loginstatus值
    将当前时间戳写入value字段
    """
    db_path = 'lwservice.db'

    try:
        # 连接到数据库
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 查询原始值
        cursor.execute("SELECT value FROM tOption WHERE name = 'loginstatus'")
        result = cursor.fetchone()

        if result is None:
            print("错误：未找到name为'loginstatus'的记录")
            return

        original_value = result[0]
        print(f"原始值: {original_value}")

        # 获取当前时间戳
        current_timestamp = int(time.time())
        current_datetime = datetime.now()

        # 更新数据库中的值
        cursor.execute("UPDATE tOption SET value = ? WHERE name = 'loginstatus'", (str(current_timestamp),))

        # 提交更改
        conn.commit()

        # 验证更新是否成功
        cursor.execute("SELECT value FROM tOption WHERE name = 'loginstatus'")
        updated_result = cursor.fetchone()
        updated_value = updated_result[0] if updated_result else "更新失败"

        # 关闭数据库连接
        conn.close()

        # 显示结果
        print(f"原始值: {original_value}")
        print(f"修改后的值: {updated_value}")
        print(f"当前时间戳: {current_timestamp}")
        print(f"可读时间: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        print("数据库更新完成！")

    except sqlite3.Error as e:
        print(f"数据库操作错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    print("开始更新loginstatus值...")
    update_loginstatus()
