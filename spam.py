#bin/bash
import base64
script = b'''
I0xpYnJlcmlhcyBhIGltcG9ydGFyCmltcG9ydCBzb2NrZXQsc3RydWN0LHRpbWUsb3Msc3lzCmZy
b20gZmFrZXIgaW1wb3J0IEZha2VyCmZyb20gY29uZmlnLmJhbm5lcnMuaW5pY2lvIGltcG9ydCAq
CmZyb20gY29uZmlnLmZ1bmNpb25lcy5sb2dpbiBpbXBvcnQgKgpmcm9tIGNvbmZpZy5mdW5jaW9u
ZXMuaW5nIGltcG9ydCAqCmZyb20gY29uZmlnLmJhbm5lcnMuY293IGltcG9ydCAqCmZyb20gY29u
ZmlnLmZ1bmNpb25lcy51c2FnZSBpbXBvcnQgKgoKI0luZm9ybWFjaW9uIGZhbHNhCgpmYWtlID0g
RmFrZXIoKQoKIyBDb2xvcmVzClZlcmRlPSJceDFiWzMybSIKUm9qbz0iXHgxYlszMW0iClJvam9i
cmlsbGFudGU9Ilx4MWJbOTFtIgoKCiNCYW5lciBkZSBpbmljaW9vCnNob3coKQojIExvZ2luIGRl
IGd1YXJkYXIgY29udHJhc2XDsWEKdHJ5OgogICBjb250cmEoKQpleGNlcHQ6CiAgIHByaW50KCJc
eDFiWzMxbUVycm9yIikKCiMgTG9naW4gZGUgdmVyaWZpY2FjaW9uIGRlIGNvbnRyYXNlw7FhCmxv
Z2lubigpCgojIENvZGlnbyBQcmluY2lwYWwKIyBGdW5jaW9uIGluZm9ybWFjaW9uIGZhbHNhCgpj
bGFzcyBwYWxhYnJhc19mYWtlcigpOgogICBkZWYgX19pbml0X18oc2VsZik6CiAgICAgIHNlbGYu
bmFtZXMgPSBmYWtlLm5hbWUoKQogICAgICBzZWxmLnRleHRvID0gZmFrZS50ZXh0KCkKZmFrZSA9
IHBhbGFicmFzX2Zha2VyKCkKCiMqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqCiMgRGlh
bG9nb28KCgoKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqCiMgTWVu
dQpzaG93digpCgojKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKgojIHBhcnRlcyBh
IGVzY29nZXIKIyBCdWNsZSB3aGlsZSBJbnB1dCBkZSBtZW51CmNsYXJvPVRydWUKCndoaWxlIGNs
YXJvPT1UcnVlOgogICB0cnk6CiAgICAgIGlucHV0X2E9aW5wdXQoIiIifFx4MWJbMzJtc3BhbVx4
MWJbMDBtfD4+PiAiIiIpCiAgIGV4Y2VwdDoKICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAg
IHByaW50KCJTY3JpcHQgRmluYWxpemFkbyA6KSIpCiAgICAgIGV4aXQoKQogICAjTWVudQoKICAg
IyoqKioqKgogICAjIEF5dWRhYSBoZWxwICoqKioqKioqKioqKioqKioqKioqCiAgIGlmIGlucHV0
X2E9PSJoYWNrIC0taGVscCI6CiAgICAgIHVzb28oKQogICAjIHBhamluYSBkZSBheXVkYSAqKioq
KioqKioqKioqKioqKgogICBlbGlmIGlucHV0X2E9PSJoYWNrIC0tcGFqaW5hX2giOgogICAgICBv
cy5zeXN0ZW0oInRlcm11eC1vcGVuLXVybCBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcHJvZmls
ZS5waHA/aWQ9MTAwMDgzMTU4OTE0MDI4IikKICAgICAjIHNwYW0gKioqKioqKioqKioqKioqKioq
KioqKioqKioqKioqKioqCiAgIGVsaWYgaW5wdXRfYT09ImhhY2sgLS1zcGFtIjoKICAgICAgY2xh
cm89RmFsc2UKICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgIG51bWVybz1pbnB1dCgiSW5n
cmVzYSBudW1lcm8gOiAiKQogICAgICBtZW5zYWplPWlucHV0KCJpbmdyZXNhIG1lbnNhamUgOiAi
KQogICAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgICAgIyBpbmZvcm1hY2lvbiBkZSBzcGFtCiAg
ICAgIGluZm9ybWFjaW9uPSIiIgoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioKICAg
IFx4MWJbMzZtSU5GT1JNQUNJT05ceDFiWzAwbQoKTnVtZXJvOiB7fQptZW5zYWplOiB7fQoKCioq
KioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKgogICAgICAiIiIuZm9ybWF0KG51bWVybyxt
ZW5zYWplKQogICAgICBwcmludChpbmZvcm1hY2lvbikKICAgICAgI0d1YXJkYSBsb3MgbnVtZXJv
cyAqKioqKioqKioqKioqKioqKioqKioqKgogICAgICBudW09b3BlbigiL2RhdGEvZGF0YS9jb20u
dGVybXV4L2ZpbGVzL2hvbWUvcHJveWVjdF9zbXMvY29uZmlnL251bWVyb3MudHh0IiwgInciKQog
ICAgICBudW0ud3JpdGUobnVtZXJvKQogICAgICBudW0uY2xvc2UoKQogICAgICAjKioqKioqKioq
KioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioKICAgICAgIyBydW4gc3BhbSAqKioqKioq
KioqKioqKioqKioqKioqCiAgICAgIHdoaWxlIGNsYXJvID09IEZhbHNlOgogICAgICAgICBydW49
aW5wdXQoIiIiCiBceDFiWzMybVshXVx4MWJbMDBtIHJ1biAgIHwKIFx4MWJbMzJtWyFdXHgxYlsw
MG0gZXhpdCAgfD4+PiAiIiIpCiAgICAgICAgIGlmICJydW4iIGluIHJ1bjoKICAgICAgICAgICAg
IHRyeToKICAgICAgICAgICAgICAgICBjbGFybz1UcnVlCiAgICAgICAgICAgICAgICAgb3Muc3lz
dGVtKCJjbGVhciIpCiAgICAgICAgICAgICAgICAgY2FudGlkYWQ9aW50KGlucHV0KCJceDFiWzMy
bVshXVx4MWJbMDBtIENhbnRpZGFkIDogIikpCiAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJj
bGVhciIpCiAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJj
bGVhciIpCiAgICAgICAgICAgICAgICAgcHJpbnQoImVycm9yIikKICAgICAgICAgICAgIGluZm9y
bWE9InRlcm11eC1zbXMtc2VuZCAtbiAiICsgbnVtZXJvICsgIiAiICsgbWVuc2FqZQogICAgICAg
ICAgICAgZm9yIHggaW4gcmFuZ2UoY2FudGlkYWQpOgogICAgICAgICAgICAgICAgIHByaW50KCJb
Iix4LCJdIiwgIiBlbnZpYWRvIGNvbiBleGl0byAgIikKICAgICAgICAgICAgICAgICBvcy5zeXN0
ZW0oaW5mb3JtYSkKICAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICAgICAgICAgICBv
cy5zeXN0ZW0oImNsZWFyIikKICAgICAgICAgICAgIHByaW50KCJceDFiWzMybVshXVx4MWJbMDBt
IFNwYW0gZmluYWxpemFkbyBjb24gZXhpdG8gIikKICAgICAgICAgICAgIHRpbWUuc2xlZXAoMikK
ICAgICAgICAgICAgIHNob3d2KCkKCiAgICAgICAgIGVsaWYgImV4aXQiIGluIHJ1bjoKICAgICAg
ICAgICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgICAgICAgICAgcHJpbnQoIjspIikKICAgICAg
ICAgICAgIGV4aXQoKQoKCiAgICMgU2FsaXIgKioqKioqKioqKioqKioqKioqKioqKioqKioqKioq
KioqKioqKioqKioqKioqKioqKioqCiAgIGVsaWYgImV4aXQiIGluIGlucHV0X2E6CiAgICAgIG9z
LnN5c3RlbSgiY2xlYXIiKQogICAgICBwcmludCgiOykiKQogICAgICBleGl0KCkKCiAgIGVsaWYg
ImhhY2sgLS1ibGFjayIgaW4gaW5wdXRfYToKICAgICAgZmY9b3BlbigiL2RhdGEvZGF0YS9jb20u
dGVybXV4L2ZpbGVzL2hvbWUvcHJveWVjdF9zbXMvY29uZmlnL251bWVyb3MudHh0IiwgInIiKQog
ICAgICBwcmludChmZi5yZWFkKCkpCiAgICAgIGZmLmNsb3NlKCkKCgoKICAgZWxzZToKICAgICBz
aG93digpCgoKCgoKCgoKCgoKCgoK'''
exec(base64.b64decode(script))
