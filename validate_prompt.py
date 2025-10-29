#!/usr/bin/env python3
"""
ClaudeHumanizer Prompt Validation Script

Validates that a phase prompt JSON file conforms to the standardization
guidelines defined in PROMPT_STANDARDS.md and PROMPT_TEMPLATE.json.

Usage:
    python validate_prompt.py <phase_file.json>
    python validate_prompt.py --all  # Check all phase files
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# ANSI color codes for terminal output
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Required top-level fields in exact order
REQUIRED_HEADER_FIELDS = [
    'title',
    'version',
    'date',
    'assembly_line_position',
    'description'
]

# Required sections that must be present
REQUIRED_SECTIONS = [
    'domain_restrictions',
    'persona',
    'agent_directives',
    'anti_hallucination_framework',
    'output_format',
    'CRITICAL_FINAL_INSTRUCTION'
]

# Standard fields in domain_restrictions
DOMAIN_RESTRICTION_FIELDS = ['only_handle', 'never_touch', 'respect_assembly_line']

# Standard never_touch items (all phases must include these)
STANDARD_NEVER_TOUCH = [
    'dialogue',
    'markdown',
    'character speech',
    'previous phases'
]

# Standard persona fields
PERSONA_FIELDS = ['name', 'background', 'expertise', 'philosophy']

# Standard agent_directives fields
AGENT_DIRECTIVE_FIELDS = ['persistence', 'tool_usage', 'deliberate_planning']

# Standard anti_hallucination_framework fields
ANTI_HALLUCINATION_FIELDS = ['real_world_facts', 'fictional_world_building', 'fallback_strategy']

# Standard output_format sub-sections
OUTPUT_FORMAT_SECTIONS = [
    'artifact_only_system',
    'artifact_specifications',
    'no_changes_handling',
    'protection_requirements',
    'output_restrictions'
]

# Discouraged field names (suggest replacements)
DISCOURAGED_NAMES = {
    'core_instructions': 'processing_instructions',
    'processing_steps': 'processing_instructions',
    'identification_rules': 'detection_criteria or detection_framework',
    'improvement_methods': 'enhancement_techniques or optimization_strategies',
    'quality_checks': 'quality_standards or quality_assurance'
}


def check_header_order(data: Dict) -> List[Tuple[str, str]]:
    """Check if header fields are in the correct order."""
    issues = []
    keys = list(data.keys())

    # Find positions of header fields
    for i, required_field in enumerate(REQUIRED_HEADER_FIELDS):
        if required_field not in data:
            issues.append(('error', f"Missing required header field: {required_field}"))
        elif required_field not in keys[:10]:
            issues.append(('warning', f"Header field '{required_field}' should be in first 10 lines"))

    # Check assembly_line_position is near the top (should be line 4)
    if 'assembly_line_position' in keys:
        pos = keys.index('assembly_line_position')
        if pos > 5:
            issues.append(('warning', f"'assembly_line_position' is at position {pos}, should be position 3-4 (line 4)"))

    return issues


def check_required_sections(data: Dict) -> List[Tuple[str, str]]:
    """Check if all required sections are present."""
    issues = []

    for section in REQUIRED_SECTIONS:
        if section not in data:
            issues.append(('error', f"Missing required section: {section}"))

    return issues


def check_domain_restrictions(data: Dict) -> List[Tuple[str, str]]:
    """Validate domain_restrictions section."""
    issues = []

    if 'domain_restrictions' not in data:
        return issues

    domain = data['domain_restrictions']

    # Check required fields
    for field in DOMAIN_RESTRICTION_FIELDS:
        if field not in domain:
            issues.append(('warning', f"domain_restrictions missing recommended field: {field}"))

    # Check never_touch contains standard items
    if 'never_touch' in domain:
        never_touch_str = ' '.join(str(item).lower() for item in domain['never_touch'])

        for standard_item in STANDARD_NEVER_TOUCH:
            if standard_item not in never_touch_str:
                issues.append(('warning', f"never_touch should include standard item: '{standard_item}'"))

    return issues


def check_persona(data: Dict) -> List[Tuple[str, str]]:
    """Validate persona section."""
    issues = []

    if 'persona' not in data:
        return issues

    persona = data['persona']

    for field in PERSONA_FIELDS:
        if field not in persona:
            issues.append(('warning', f"persona missing standard field: {field}"))

    return issues


def check_agent_directives(data: Dict) -> List[Tuple[str, str]]:
    """Validate agent_directives section."""
    issues = []

    if 'agent_directives' not in data:
        return issues

    directives = data['agent_directives']

    for field in AGENT_DIRECTIVE_FIELDS:
        if field not in directives:
            issues.append(('warning', f"agent_directives missing standard field: {field}"))

    # Check for extra fields
    extra_fields = set(directives.keys()) - set(AGENT_DIRECTIVE_FIELDS)
    if extra_fields:
        issues.append(('info', f"agent_directives has non-standard fields: {', '.join(extra_fields)}"))

    return issues


def check_anti_hallucination(data: Dict) -> List[Tuple[str, str]]:
    """Validate anti_hallucination_framework section."""
    issues = []

    if 'anti_hallucination_framework' not in data:
        return issues

    framework = data['anti_hallucination_framework']

    for field in ANTI_HALLUCINATION_FIELDS:
        if field not in framework:
            issues.append(('warning', f"anti_hallucination_framework missing standard field: {field}"))

    return issues


def check_output_format(data: Dict) -> List[Tuple[str, str]]:
    """Validate output_format section."""
    issues = []

    if 'output_format' not in data:
        return issues

    output_fmt = data['output_format']

    for section in OUTPUT_FORMAT_SECTIONS:
        if section not in output_fmt:
            issues.append(('warning', f"output_format missing standard section: {section}"))

    return issues


def check_discouraged_names(data: Dict) -> List[Tuple[str, str]]:
    """Check for discouraged field names."""
    issues = []

    for key in data.keys():
        if key in DISCOURAGED_NAMES:
            issues.append(('info', f"Discouraged field name '{key}', consider '{DISCOURAGED_NAMES[key]}'"))

    return issues


def validate_prompt(filepath: Path) -> Tuple[int, int, int]:
    """
    Validate a single prompt file.

    Returns: (error_count, warning_count, info_count)
    """
    print(f"\n{BOLD}Validating: {filepath.name}{RESET}")
    print("=" * 60)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"{RED}✗ ERROR: Invalid JSON - {e}{RESET}")
        return (1, 0, 0)
    except Exception as e:
        print(f"{RED}✗ ERROR: Could not read file - {e}{RESET}")
        return (1, 0, 0)

    # Skip template file
    if filepath.name == 'PROMPT_TEMPLATE.json':
        print(f"{YELLOW}ℹ Skipping template file{RESET}")
        return (0, 0, 0)

    # Collect all issues
    all_issues = []
    all_issues.extend(check_header_order(data))
    all_issues.extend(check_required_sections(data))
    all_issues.extend(check_domain_restrictions(data))
    all_issues.extend(check_persona(data))
    all_issues.extend(check_agent_directives(data))
    all_issues.extend(check_anti_hallucination(data))
    all_issues.extend(check_output_format(data))
    all_issues.extend(check_discouraged_names(data))

    # Count issues by severity
    errors = [issue for issue in all_issues if issue[0] == 'error']
    warnings = [issue for issue in all_issues if issue[0] == 'warning']
    infos = [issue for issue in all_issues if issue[0] == 'info']

    # Display issues
    for severity, message in errors:
        print(f"{RED}✗ ERROR: {message}{RESET}")

    for severity, message in warnings:
        print(f"{YELLOW}⚠ WARNING: {message}{RESET}")

    for severity, message in infos:
        print(f"ℹ INFO: {message}")

    # Summary
    if not all_issues:
        print(f"\n{GREEN}✓ All checks passed!{RESET}")
    else:
        print(f"\n{BOLD}Summary:{RESET}")
        if errors:
            print(f"{RED}  Errors: {len(errors)}{RESET}")
        if warnings:
            print(f"{YELLOW}  Warnings: {len(warnings)}{RESET}")
        if infos:
            print(f"  Info: {len(infos)}")

    return (len(errors), len(warnings), len(infos))


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_prompt.py <phase_file.json>")
        print("       python validate_prompt.py --all")
        sys.exit(1)

    script_dir = Path(__file__).parent

    if sys.argv[1] == '--all':
        # Validate all phase files
        phase_files = sorted(script_dir.glob('[0-9]*.json'))

        if not phase_files:
            print("No phase files found in current directory")
            sys.exit(1)

        print(f"{BOLD}Validating {len(phase_files)} phase files...{RESET}")

        total_errors = 0
        total_warnings = 0
        total_infos = 0

        for filepath in phase_files:
            errors, warnings, infos = validate_prompt(filepath)
            total_errors += errors
            total_warnings += warnings
            total_infos += infos

        # Overall summary
        print(f"\n{BOLD}{'=' * 60}{RESET}")
        print(f"{BOLD}OVERALL SUMMARY:{RESET}")
        print(f"  Files validated: {len(phase_files)}")

        if total_errors > 0:
            print(f"{RED}  Total errors: {total_errors}{RESET}")
        else:
            print(f"{GREEN}  Total errors: 0{RESET}")

        if total_warnings > 0:
            print(f"{YELLOW}  Total warnings: {total_warnings}{RESET}")
        else:
            print(f"  Total warnings: 0")

        print(f"  Total info: {total_infos}")

        if total_errors == 0 and total_warnings == 0:
            print(f"\n{GREEN}{BOLD}✓ All prompts conform to standards!{RESET}")
            sys.exit(0)
        else:
            sys.exit(1)

    else:
        # Validate single file
        filepath = Path(sys.argv[1])

        if not filepath.exists():
            print(f"{RED}ERROR: File not found: {filepath}{RESET}")
            sys.exit(1)

        errors, warnings, infos = validate_prompt(filepath)

        if errors > 0:
            sys.exit(1)
        else:
            sys.exit(0)


if __name__ == '__main__':
    main()
