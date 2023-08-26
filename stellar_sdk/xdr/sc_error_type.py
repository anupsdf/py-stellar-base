# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
from __future__ import annotations

import base64
from enum import IntEnum

from xdrlib3 import Packer, Unpacker

__all__ = ["SCErrorType"]


class SCErrorType(IntEnum):
    """
    XDR Source Code::

        enum SCErrorType
        {
            SCE_CONTRACT = 0,
            SCE_WASM_VM = 1,
            SCE_CONTEXT = 2,
            SCE_STORAGE = 3,
            SCE_OBJECT = 4,
            SCE_CRYPTO = 5,
            SCE_EVENTS = 6,
            SCE_BUDGET = 7,
            SCE_VALUE = 8,
            SCE_AUTH = 9
        };
    """

    SCE_CONTRACT = 0
    SCE_WASM_VM = 1
    SCE_CONTEXT = 2
    SCE_STORAGE = 3
    SCE_OBJECT = 4
    SCE_CRYPTO = 5
    SCE_EVENTS = 6
    SCE_BUDGET = 7
    SCE_VALUE = 8
    SCE_AUTH = 9

    def pack(self, packer: Packer) -> None:
        packer.pack_int(self.value)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> SCErrorType:
        value = unpacker.unpack_int()
        return cls(value)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> SCErrorType:
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> SCErrorType:
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)