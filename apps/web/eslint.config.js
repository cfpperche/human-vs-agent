import tseslint from "typescript-eslint";

export default tseslint.config(
  { ignores: ["node_modules", "src/generated"] },
  ...tseslint.configs.recommended,
);
