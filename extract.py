#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import shutil
import os
import sys

files = [
    'Helpers/Razor/HtmlExtensions/Nl2brExtension.cs',
    'Helpers/Razor/HtmlClasses.cs',
    'Helpers/Razor/HtmlHelpers.cs',
    'Helpers/Razor/TemplatesConsts.cs',
    'Helpers/FlashMessage.cs',
    'Modules/Shared/Views/Partial/DisplayTemplates/Boolean.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/Currency.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/Date.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/DateTime.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/Decimal.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/DisplayBase.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/EmailAddress.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/MultilineText.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/Number.cshtml',
    'Modules/Shared/Views/Partial/DisplayTemplates/String.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Boolean.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Currency.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Date.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/DateTime.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Decimal.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/DropDown.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/EmailAddress.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Enum.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/HttpPostedFileBase.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Int32.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/MultilineText.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Password.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Single.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/String.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/Text.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/TextBoxBase.cshtml',
    'Modules/Shared/Views/Partial/EditorTemplates/TimeSpan.cshtml',
    'Modules/Shared/Views/Partial/_FlashMessages.cshtml'
]
content_dir = 'content/'
generic_namespace = '$rootnamespace$'

# Copy files
parser = argparse.ArgumentParser(description='Resources extracter')
parser.add_argument('--solution', required=True)
parser.add_argument('--namespace', required=True)
args = parser.parse_args()

solution_path = args.solution
if not os.path.isdir(solution_path):
    print('Could not find solution directory {}'.format(solution_path))
    sys.exit(1)

# Find files in solution
print('Extracting files from solution...')
for file_path in files:
    # Copy file to this directory
    src_path = os.path.join(solution_path, file_path)
    dest_path = os.path.join(content_dir, file_path) + '.pp'

    if not os.path.isfile(src_path):
        print('Could not find resource {}'.format(src_path))
        sys.exit(1)

    shutil.copy(src_path, dest_path)
    print('  - {}'.format(file_path))

    # Update namespace
    lines = []
    with open(dest_path, 'r') as fh:
        for line in fh:
            if args.namespace in line:
                line = line.replace(generic_namespace, args.namespace)

            lines.append(line)

    with open(dest_path, 'w') as fh:
        for line in lines:
            fh.write(line)
