from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', defaults={'filename': 'file1.txt'},methods=['GET'])
@app.route('/<filename>',methods=['GET'])
def read_file(filename):
    # breakpoint()
    start_line = request.args.get('start', type=int)
    end_line = request.args.get('end', type=int)

    try:
        # Construct file path
        file_path = os.path.join('files', filename)

        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{filename}' not found.")

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Check if both start_line and end_line are provided and within bounds
        if start_line is not None and end_line is not None:
            if start_line <= 0 or end_line <= 0 or start_line > end_line:
                raise ValueError("Invalid start_line or end_line values.")
            lines = lines[start_line - 1:end_line]

        return render_template('display.html', content=''.join(lines))
    except FileNotFoundError as e:
        return render_template('error.html', error=str(e))
    except ValueError as e:
        return render_template('error.html', error=str(e))
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
