from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reminders = []
next_id = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id
    if request.method == 'POST':
        medicine = request.form.get('medicine')
        time = request.form.get('time')
        edit_id = request.form.get('edit_id')

        if medicine and time:
            if edit_id:
                for r in reminders:
                    if r['id'] == int(edit_id):
                        r['medicine'] = medicine
                        r['time'] = time
                        break
            else:
                reminders.append({
                    'id': next_id,
                    'medicine': medicine,
                    'time': time
                })
                next_id += 1

        return redirect(url_for('index'))

    return render_template('index.html', reminders=reminders)

@app.route('/delete/<int:reminder_id>', methods=['POST'])
def delete(reminder_id):
    global reminders
    reminders = [r for r in reminders if r['id'] != reminder_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
