# License-Key-Generator
A Python GUI application built using the customtkinter library for generating license keys in bulk with customizable settings.
### Features:
- Simple and modern interface.
- Dark mode (only dark mode is available) and light mode (coming in the future) for user preference.
- Generate keys button activates when file type and save location are selected.
- Keys Settings tab allows users to customize generated keys:
  - Key length adjustment.
  - Option to include/exclude numbers in generated keys.
- Option to choose the file type for generated keys.
- Browse feature for selecting the save location of generated keys.
- Ability to specify the amount of keys to generate.

### Usage:
1. Select file type for generated keys.
2. Choose save location for the generated keys.
3. Customize key settings as per preference.
4. Click on "Generate keys" to generate the keys.

### Note:
- It is recommended to create a folder for saving generated files.
- It is currently still Console based.

### Will there ever be two identical keys?
While the probability of generating two identical keys is extremely low, it’s not zero. Given a large enough number of keys and/or a small enough key length, there’s a chance that two or more generated keys could be the same due to the random nature of the key generation process. 

### Who is it for?:
The Mass License Key Generator GUI is designed for developers, businesses, and organizations requiring a streamlined solution for generating large quantities of unique license keys. It caters to software companies, digital product distributors, small businesses, educational institutions, freelancers, security professionals, and DRM solution providers, offering customizable settings and a user-friendly interface to meet a variety of licensing needs efficiently.

### legality:
The legality of using the Mass License Key Generator GUI depends on how the generated license keys are utilized. If the keys are generated and used in compliance with applicable laws, licensing agreements, and terms of service, it is considered legal. However, distributing or using license keys without proper authorization or in violation of software licenses and intellectual property rights may lead to legal consequences. Users should ensure that they have the necessary rights and permissions to generate and use license keys in accordance with legal standards. And as the creator of the Mass License Key Generator GUI, I cannot be held responsible for any misuse or unauthorized distribution of the generated license keys. Users assume full responsibility for the lawful and ethical use of the tool, including compliance with relevant laws, licensing agreements, and intellectual property rights. Additionally, I recommend users exercise caution and diligence in their use of the software to avoid any potential legal or ethical issues. Technically, it’s possible for the same license key to be generated more than once, but in practice, it’s highly unlikely if the key length is sufficiently large and the number of keys generated is not excessively high. To combat this in the future I will be adding check to your key generation process to ensure no duplicate keys are produced. This will be done by storing all generated keys in a set (which only holds unique values) and checking each new key against this set. If a duplicate is found, a new key should be generated.
