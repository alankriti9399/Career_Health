import streamlit as st
import subprocess
import os

def main():
    st.title("Run External Python Script")
    
    # Button to trigger the Python file
    if st.button("Run Script"):
        try:
            # Ensure the script exists in the same directory
            script_path = os.path.join(os.getcwd(), "main (1).py")
            if os.path.exists(script_path):
                # Run the script
                result = subprocess.run(
                    ["python", script_path],
                    capture_output=True,
                    text=True
                )
                # Display the output of the script
                st.success("Script executed successfully!")
                st.text("Output:")
                st.code(result.stdout)
                if result.stderr:
                    st.error("Errors:")
                    st.code(result.stderr)
            else:
                st.error("Script file 'main.py' not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
