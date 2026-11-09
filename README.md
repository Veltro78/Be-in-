# Le Grand Passage

Jeu idle web en 3D, style « Aero Lagoon » (années 2006) : faites passer l'humanité entière (8,1 milliards) par une seule porte tournante en verre, au milieu d'un lagon.

**Jouer** : ouvrez `index.html` dans un navigateur (mobile ou ordinateur). Aucun build : Three.js est fourni dans `lib/`.

## Comment jouer
- **Touchez** l'écran : la porte reçoit une impulsion. **Maintenez** : elle accélère.
- Chaque bonhomme qui traverse rapporte des pièces. Un flux continu fait monter le **combo** (jusqu'à ×6).
- Les bonhommes **orange** sont des VIP : ×25.
- Achetez des améliorations dans la barre du bas ; de nouvelles se débloquent au fil des passages :
  Rotation, Capacité, Affluence, Pales, Mégaphone, Monorail, Moteur, Foule.
- Sauvegarde automatique + gains hors-ligne (jusqu'à 3 h).
- Menu pause : son, qualité (haute / économie sans ombres), remise à zéro.

## Agent Pack
`.claude/agents/pack.md` définit **Pack**, l'agent Claude Code chargé de faire évoluer ce jeu
(nouvelles mécaniques, équilibrage, effets). Exemple : « Pack, ajoute un événement de foule géante toutes les 5 minutes ».
