import os
import subprocess

def run_test(input_file, output_file, options):
    """Run converter with specified options and print result"""
    cmd = ["py", "converter.py", input_file] + options
    if output_file:
        cmd.extend(["-o", output_file])
    
    print(f"\nTesting: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Output: {result.stdout.strip()}")
    if result.stderr:
        print(f"Errors: {result.stderr.strip()}")
    
    if os.path.exists(output_file or input_file.replace('.png', '.svg')):
        print("[PASS] SVG file created successfully")
    else:
        print("[FAIL] Failed to create SVG file")

def main():
    print("Testing PNG/JPG to SVG Converter")
    print("================================")

    # Test 1: Basic conversion
    run_test("examples/simple_shapes.png", "examples/test1.svg", [])

    # Test 2: Color preservation
    run_test("examples/simple_shapes.png", "examples/test2.svg", ["--color"])

    # Test 3: High detail settings
    run_test("examples/pattern.png", "examples/test3.svg", 
             ["--color", "--edge-threshold", "50", "--contrast", "1.2"])

    # Test 4: Black and white with blur
    run_test("examples/pattern.png", "examples/test4.svg", 
             ["--blur", "2", "--edge-threshold", "150"])

if __name__ == "__main__":
    main()
