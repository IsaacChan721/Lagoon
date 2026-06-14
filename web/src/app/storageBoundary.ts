export type StorageBoundary = {
  mode: "local-only";
  metadata: "sqlite";
  vault: "encrypted-local-vault";
  contentUploadDefault: "blocked";
  rawContentInRepo: "forbidden";
};

export const storageBoundary: StorageBoundary = {
  mode: "local-only",
  metadata: "sqlite",
  vault: "encrypted-local-vault",
  contentUploadDefault: "blocked",
  rawContentInRepo: "forbidden",
};

