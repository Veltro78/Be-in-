# Le Grand Passage

Jeu idle web en 3D, style « Néon de nuit » : une rue de ville sous la pluie, des taxis et un bus de nuit déposent une foule de figurines peintes que vous faites passer, jusqu'aux 8,1 milliards d'humains, par une seule porte tournante.

**Jouer** : ouvrez `index.html` dans un navigateur (mobile ou ordinateur). Aucun build : Three.js est fourni dans `lib/`.

## Comment jouer
- Écran titre : touchez pour lancer la partie (active aussi le son et la musique).
- **Touchez** l'écran : la porte reçoit une impulsion. **Maintenez** : elle accélère.
- Chaque bonhomme qui traverse rapporte des pièces. Un flux continu fait monter le **combo** (jusqu'à ×6).
- Les figurines en costume **doré** sont des VIP : ×25.
- Paliers de flux (Bien ! → Super ! → … → Cosmique !) annoncés en grand, avec son et bulles.
- **Jauge RUSH** : elle se remplit en touchant, en maintenant et à chaque passage. Pleine, elle déclenche 10 s de RUSH ×3 (porte dorée, musique accélérée).
- **Jetons dorés** : de temps en temps, un jeton doré flotte au-dessus de la place ; touchez-le avant qu'il disparaisse pour un gros bonus.
- Au lancement, la porte tombe du ciel et les néons s'allument.
- **Paliers** (10, 25, 50, 100… humains passés) : bannière + pièces bonus.
- Les pièces gagnées volent jusqu'au compteur, qui défile.
- Achetez des améliorations dans la barre du bas ; de nouvelles se débloquent au fil des passages :
  Rotation, Capacité, Affluence, Pales, Mégaphone, Bus de nuit, Moteur, Foule.
- Sauvegarde automatique + gains hors-ligne (jusqu'à 3 h).
- Menu pause : son, qualité (haute / économie sans ombres), remise à zéro.

## Agent Pack
`.claude/agents/pack.md` définit **Pack**, l'agent Claude Code chargé de faire évoluer ce jeu
(nouvelles mécaniques, équilibrage, effets). Exemple : « Pack, ajoute un événement de foule géante toutes les 5 minutes ».

## Version Artifact (claude.ai)
`python3 tools/build-artifact.py sortie.html` produit la version publiable comme Artifact :
mêmes fichiers, mais Three.js est chargé depuis jsDelivr (three@0.158.0) au lieu de `lib/`.
